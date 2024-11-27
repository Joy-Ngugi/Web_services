import xml.etree.ElementTree as ET

data = """
<users>
    <user id="1">
        <name>Alice</name>
        <email>alice@example.com</email>
        <phone>+2547890645321</phone>
    </user>
    <user id="2">
        <name>Bob</name>
        <email>bob@example.com</email>
        <phone>+25478456372017</phone>
    </user>
    <user id="3">
        <name>James</name>
        <email>james@example.com</email>
        <phone>+25471236372999</phone>
    </user>
</users>
"""

# Parse XML
root = ET.fromstring(data)

# Access elements
for user in root.findall('user'):
    name = user.find('name').text
    email = user.find('email').text
    phone_number = user.find('phone').text
    print(f"Name: {name}, Email: {email}, Phone Number:{phone_number}")
