import requests

# Test alert info
alert = {
    "event": "⚠️ TEST: Tornado Warning",
    "description": "This is a test alert. No action is required.",
    "effective": "Now",
    "location": "Test County, TX",
    "link": "https://www.weather.gov/"
}

# Format message
message = f"""**{alert['event']}**
{alert['description']}

⏰ **Effective**: {alert['effective']}
📍 **Location**: {alert['location']}
🔗 [More Info]({alert['link']})
"""

# Send via Notify.Events
res = requests.post("https://notify.events/api/send", data={
    "token": "s1p04c9pxnq303h43kgpojrfo7g-ncd1",  # replace with your real token
    "message": message
})

print("Status:", res.status_code)
print("Response:", res.text)
