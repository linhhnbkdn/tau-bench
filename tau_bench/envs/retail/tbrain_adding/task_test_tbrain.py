from tau_bench.types import Task, Action

TASKS_TEST = [
    Task(
        annotator="4",
        user_id="harper_santos_8115",
        instruction="You name is Santos Harper and your email is harper.santos8390@example.com. You mistake when input email and update to tbranin@emample.com email",
        actions=[
            Action(
                name="find_user_id_by_email",
                kwargs={"email": "harper.santos8390@example.com"},
            ),
            Action(
                name="modify_user_email",
                kwargs={
                    "user_id": "harper_santos_8115",
                    "email": "tbranin@emample.com",
                },
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="4",
        user_id="harper_santos_8115",
        instruction="You name is Santos Harper and your email is harper.santos8390@example.com. You only want to cancel #W5765742 order because you change your mind",
        actions=[
            Action(
                name="find_user_id_by_email",
                kwargs={"email": "harper.santos8390@example.com"},
            ),
            Action(name="get_user_details", kwargs={"user_id": "harper_santos_8115"}),
            Action(name="get_order_details", kwargs={"order_id": "#W5765742"}),
        ],
        outputs=[],
    ),
]
