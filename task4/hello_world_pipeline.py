from prefect import task, flow

@task
def say_hello():
    print("Hello, world!")

@flow(name="Hello World Flow")
def hello_world_flow():
    say_hello()

if __name__ == "__main__":
    hello_world_flow()
