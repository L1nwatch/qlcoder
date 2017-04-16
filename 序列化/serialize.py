from protobuf3.message import Message
from enum import Enum
from protobuf3.fields import StringField, EnumField, MessageField, Int32Field


class Task(Message):

    class AnswerType(Enum):
        STRING = 0
        INT = 1
        DOUBLE = 2

    class Answer(Message):
        pass


class AddTask(Message):
    pass

Task.Answer.add_field('data', Int32Field(field_number=1, required=True))
Task.Answer.add_field('type', EnumField(field_number=2, optional=True, enum_cls=Task.AnswerType, default=Task.AnswerType.INT))
Task.add_field('id', Int32Field(field_number=1, required=True))
Task.add_field('title', StringField(field_number=2, optional=True))
Task.add_field('content', StringField(field_number=3, optional=True))
Task.add_field('score', Int32Field(field_number=4, required=True))
Task.add_field('author', StringField(field_number=5, optional=True))
Task.add_field('answer', MessageField(field_number=6, repeated=True, message_cls=Task.Answer))
AddTask.add_field('task', MessageField(field_number=1, repeated=True, message_cls=Task))
