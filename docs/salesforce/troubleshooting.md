---
published: true
---
# Troubleshooting

## Postman: Session expired or invalid
**Problem:** When calling a REST API (with Postman) you receive the following response, despite your access token being valid:

```json
[{"message":"Session expired or invalid","errorCode":"INVALID_SESSION_ID"}]
```

The root cause is a "wrong" URL in the variables `url` and `_endpoint`.

**Solution:** As described in the [Trailblazer Community](https://trailhead.salesforce.com/trailblazer-community/feed/0D54V00007T4U1tSAF), either:

- Enable the setting `Follow Authorization header` for the call or
- Set the correct URL for the environment variables `url` and `_endpoint`. The correct URL is the one ending with `.my.salesforce.com` resp. `.sandbox.my.salesforce.com` (shown on the login screen).