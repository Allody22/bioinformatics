#!/bin/bash

samtools flagstat alignment_sorted.bam > flagstat_output.txt

total_reads=$(grep "in total" flagstat_output.txt | awk '{print $1}')
mapped_reads=$(grep "mapped (" flagstat_output.txt | head -n 1 | awk '{print $1}')
mapped_percentage=$(echo "scale=2; ($mapped_reads/$total_reads)*100" | bc)

echo "Total reads: $total_reads"
echo "Mapped reads: $mapped_reads"
echo "Mapped reads percentage: $mapped_percentage%"

# Проверка качества картирования
if (( $(echo "$mapped_percentage > 90" | bc -l) )); then
    echo "Quality Check: OK - $mapped_percentage%"
elif (( $(echo "$mapped_percentage > 80" | bc -l) )); then
    echo "Quality Check: GOOD - $mapped_percentage%"
else
    echo "Quality Check: BAD - $mapped_percentage%"
fi