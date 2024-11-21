from fastapi import FastAPI, BackgroundTasks
import asyncio

app = FastAPI()

async def task_one():
    # do something here
    await asyncio.sleep(5)
    print("task_one success")

async def task_two():
    # do something else here
    await asyncio.sleep(10)
    print("task_two success")

@app.post("/start_tasks")
async def start_tasks(background_tasks: BackgroundTasks):
    background_tasks.add_task(task_one)
    background_tasks.add_task(task_two)
    return {"message": "Tasks started successfully!"}

@app.get('/')
def hello_world():
    return "Hello,World"

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)