import logging.config
from prefect import task, flow, get_run_logger
import subprocess

# Настройка логгирования для записи в файл
logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file_handler": {
            "class": "logging.FileHandler",
            "filename": "pipeline_log.txt",
            "mode": "w",
            "encoding": "utf-8",
            "formatter": "custom",
        },
    },
    "formatters": {
        "custom": {
            "format": "%(asctime)s | %(name)s | %(levelname)s | %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        },
    },
    "root": {
        "handlers": ["file_handler"],
        "level": "INFO",
    },
}

# Применение конфигурации логгирования
logging.config.dictConfig(logging_config)

@task
def run_flagstat():
    logger = get_run_logger()
    logger.info("Запуск samtools flagstat через WSL...")

    # Выполнение команды через WSL
    result = subprocess.run(["wsl", "samtools", "flagstat", "alignment_sorted.bam"], capture_output=True, text=True)

    # Сохранение вывода в файл
    with open("flagstat_output_pipeline.txt", "w", encoding="utf-8") as f:
        f.write(result.stdout)

    logger.info("Файл flagstat_output_pipeline.txt создан.")
    return result.stdout

@task
def analyze_flagstat():
    logger = get_run_logger()
    logger.info("Анализируем файл flagstat_output_pipeline.txt...")
    with open("flagstat_output_pipeline.txt", encoding="utf-8") as f:
        lines = f.readlines()
    total_reads = int(lines[0].split()[0])
    mapped_reads = int(lines[6].split()[0])
    mapped_percentage = (mapped_reads / total_reads) * 100
    logger.info(f"Процент картированных ридов: {mapped_percentage:.2f}%")
    if mapped_percentage > 90:
        return "VERY OK " + str(mapped_percentage)
    elif mapped_percentage > 80:
        return "GOOD " + str(mapped_percentage)
    else:
        return "BAD " + str(mapped_percentage)

@flow(name="Mapping Quality Assessment")
def mapping_quality_assessment():
    logger = get_run_logger()
    logger.info("Запуск пайплайна оценки качества картирования")
    run_flagstat()
    quality_check = analyze_flagstat()
    logger.info(f"Результат оценки качества картирования: {quality_check}")

if __name__ == "__main__":
    mapping_quality_assessment()
