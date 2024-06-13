import os

from dotenv import load_dotenv
from sqlalchemy.orm import Session
from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Updater

from .database import get_db
from .models import Base, Task, engine

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

Base.metadata.create_all(bind=engine)


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Welcome! Use /add <task> to add a task and /tsk to list all tasks."
    )


def add(update: Update, context: CallbackContext) -> None:
    db: Session = next(get_db())
    task_description = " ".join(context.args)
    if not task_description:
        update.message.reply_text("Usage: /add <task description>")
        return

    new_task = Task(description=task_description)
    db.add(new_task)
    db.commit()
    update.message.reply_text(f"Task added: {task_description}")


def list_tasks(update: Update, context: CallbackContext) -> None:
    db: Session = next(get_db())
    tasks = db.query(Task).all()
    if not tasks:
        update.message.reply_text("No tasks found.")
    else:
        tasks_list = "\n".join(
            [
                f"{task.id}. {task.description} (added on {task.created_at})"
                for task in tasks
            ]
        )
        update.message.reply_text(f"Tasks:\n{tasks_list}")


def main() -> None:
    updater = Updater(TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("add", add))
    dispatcher.add_handler(CommandHandler("tsk", list_tasks))

    updater.start_polling()
    updater.idle()
