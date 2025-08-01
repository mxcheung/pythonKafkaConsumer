Avoid this

```
def message_handler(msg):
    producer = Producer({...})         # BAD: Re-initializing each time
    producer.produce(...)              # Send message
    producer.flush()                   # BAD: Flush on every message
```
