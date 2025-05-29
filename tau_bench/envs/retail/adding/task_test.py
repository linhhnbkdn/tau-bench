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
    Task(
        annotator="4",
        user_id="harper_santos_8115",
        instruction="Your name is Santos Harper and your email is harper.santos8390@example.com. "
        "You want to update your email to harper.santos1010@example.com to receive notifications. "
        "You received consultation from an agent about the laptop you ordered under order number #W4941028, "
        "and you would like to exchange it for a new one with an i7 processor, 8GB RAM, and 1TB SSD. "
        "You want to know how much you need to pay today in total, and you also want to cancel other orders "
        "and find out the total amount you can get refunded.",
        actions=[
            Action(
                name="find_user_id_by_email",
                kwargs={"email": "harper.santos8390@example.com"},
            ),
            Action(
                name="modify_user_email",
                kwargs={
                    "user_id": "harper_santos_8115",
                    "email": "harper.santos1010@example.com",
                },
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W4941028"},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "#4760268021"},
            ),
            Action(
                name="exchange_delivered_order_items",
                kwargs={
                    "order_id": "#W4941028",
                    "item_ids": ["3265035808"],
                    "new_item_ids": ["9844888101"],
                    "payment_method_id": "paypal_2870241",
                },
            ),
            Action(
                name="cancel_pending_order",
                kwargs={"order_id": "#W6629830", "reason": "no longer needed"},
            ),
            Action(
                name="calculate",
                kwargs={"expression": "3997.94"},
            ),
        ],
        outputs=[],
    ),
    Task(
        annotator="4",
        user_id="aarav_brown_3744",
        instruction="Your name is Briown Aarav and your email is aarav.brown3708@example.com. "
        "You would like to cancel order #W6584521, and modify the remaining order by replacing the Wristwatch with the same Bicycle from order #W6584521."
        "You also want to know the total amount you need to pay today.",
        actions=[
            Action(
                name="find_user_id_by_email",
                kwargs={"email": "aarav.brown3708@example.com."},
            ),
            Action(
                name="get_product_details",
                kwargs={"product_id": "9783735446"},
            ),
            Action(
                name="cancel_pending_order",
                kwargs={"order_id": "#W6584521", "reason": "no longer needed"},
            ),
            Action(
                name="modify_pending_order_items",
                kwargs={
                    "order_id": "#W6629830",
                    "item_ids": ["9112290483"],
                    "new_item_ids": ["7758198585"],
                    "payment_method_id": "credit_card_3627996",
                },
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W6584521"},
            ),
            Action(
                name="get_order_details",
                kwargs={"order_id": "#W5065081"},
            ),
            Action(
                name="calculate",
                kwargs={"expression": "6759.33 - 1917.21 + 1925.16"},
            ),
        ],
        outputs=[],
    ),
]
