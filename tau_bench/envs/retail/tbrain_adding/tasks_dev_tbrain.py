from tau_bench.types import Task, Action

TASKS_DEV = [
    Task(
        annotator="",
        user_id="noah_brown_6181",
        instruction="Your name is Noah and your email is noah.brown7922@example.com. You wanna change your email to tbbrain@example.com",
        actions=[
            Action(
                name="modify_user_email",
                kwargs={
                    "user_id": "noah_brown_6181",
                    "email": "tbbrain@example.com",
                },
            )
        ],
        outputs=[],
    ),
]
