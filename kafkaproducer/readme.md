Avoid this

```
def message_handler(msg):
    producer = Producer({...})         # BAD: Re-initializing each time
    producer.produce(...)              # Send message
    producer.flush()                   # BAD: Flush on every message
```

✅ Refactored Handler Pattern (Best Practice)
Restructure so:

Kafka Producer is created once (e.g., in app startup or singleton).

message_handler just calls produce(), no flush.

Delivery is handled via callbacks.

Flush only happens on ECS task shutdown.
