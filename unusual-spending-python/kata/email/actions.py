#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import uuid

def send_email(user_id: uuid.UUID, subject: str, body: str):
    print(f"Email send to {user_id}: with subject: {subject} and body:{body}")