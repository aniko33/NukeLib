<div align="center">
  <h1>NUKELIB</h1>
</div>
<div align="center">
  <img src="https://user-images.githubusercontent.com/76649588/194594113-51e9ae21-6dd4-41f3-91a5-f5a44f0bd9c3.png" alt="How-work" width="700"/>
</div>

## Index

- Features

- Installation
  
  - Prerequisites
  
  - PIP

- How work (Diagram)

- Docs
  
  - Quick start
  
  - account_info
  
  - country_code
  
  - user_lookup
  
  - server_lookup
  
  - leave_all_servers
  
  - spam_server
  
  - friends_remover
  
  - block_all

- Bugs and additions

- Contributors

- License

## Features

- Simplicity of integration

- Easy to use

- Editable by everyone

- Using HTTP/S requests to Discord

- Discord API v8/9

- Using Discord and Discord canary API

## Installation

### Prerequisites

This is a Python module, to start using this module you ***need to install [Python](https://python.org).***

***After installing Python you will have installed "[PIP](https://docs.python.org/3/installing/index.html)".***
You will be able to install with the "***[PyPI](https://pypi.org/project/nukelib/)" repositories***.

### PIP

***After doing all the prerequisites***, you have to ***open the terminal*** and then ***run this command***:

```bash
pip install nukelib
```

***now you will have the library available***

## How work (Diagram)
<img src="https://user-images.githubusercontent.com/76649588/194584868-203c5c54-147e-43ed-b795-1f663f49a0dd.png" alt="How-work" width="700"/>

### Docs

#### Quick start

You must have the ***token of the account*** you want to use, to get the token of an account ***follow this video***: [Video](https://www.youtube.com/watch?v=1dva3YqBI2E)

After obtaining the Discord token you can use the library ***without any limitations.***

###### Output

You can use this output using the **JSON** library: [Guide](https://www.w3schools.com/python/python_json.asp), [Docs](https://docs.python.org/3/library/json.html)

#### account_info

```python
#import lib
import nukelib
#insert token
token = "MFA-XXX-XXX-XXX"
#get output (JSON)
output = nukelib.account_info(token)
#show the output
print(output)
```

###### the output will be this:

```json
{
   "id":"976073855317717032",
   "username":"SitDownG0D.",
   "avatar":"23bc602fde399bec073aff31c6ba85b8",
   "avatar_decoration":"None",
   "discriminator":"3935",
   "public_flags":0,
   "flags":0,
   "banner":"None",
   "banner_color":"None",
   "accent_color":"None",
   "bio":"",
   "locale":"it",
   "nsfw_allowed":true,
   "mfa_enabled":false,
   "premium_type":0,
   "email":"test@rambler.ru",
   "verified":true,
   "phone":"None"
}
```

#### country_code

```python
#import lib
import nukelib
#insert token
token = "MFA-XXX-XXX-XXX"
#get output (Text)
output = nukelib.country_code(token)
#show the output
print(output)
```

###### the output will be this:

```json
IT
```

***In this case from non-JSON output***

#### user_lookup

```python
#import lib
import nukelib
#insert token
token = "MFA-XXX-XXX-XXX"
#enter user_id
user_id = "33495202794xxxxxx" 
#get output (JSON)
output = nukelib.user_lookup(user_id,token)
#show the output
print(output)
```

###### the output will be this:

```json
{
   "user":{
      "id":"967146351462871110",
      "username":"Mr",
      "avatar":"e926ac9e07784b5f3f9a15b9c6f6a6dd",
      "avatar_decoration":"None",
      "discriminator":"3748",
      "public_flags":0,
      "flags":0,
      "banner":"None",
      "banner_color":"None",
      "accent_color":"None",
      "bio":"https://r.honeygain.me/NIXXXXX\nhttps://earnapp.com/i/XXXe75z"
   },
   "connected_accounts":[

   ],
   "premium_since":"None",
   "premium_type":"None",
   "premium_guild_since":"None",
   "profile_themes_experiment_bucket":-1,
   "user_profile":{
      "bio":"https://r.honeygain.me/NICOLxFXXx\nhttps://earnapp.com/i/xxxe75z",
      "accent_color":"None"
   }
}
```

### server_lookup

```python
#import lib
import nukelib
#insert token
token = "MFA-XXX-XXX-XXX"
#enter server_id
server_id = "33495202794xxxxxx" 
#get output (JSON)
output = nukelib.server_lookup(server_id,token)
#show the output
print(output)
```

###### the output will be this:

```json
{
   "id":"739940211911426148",
   "name":"Decks Team",
   "icon":"a_5ec01b96f747903d17528971e988b67a",
   "description":"None",
   "splash":"6bc47982e4d3d302146fed104b073e96",
   "discovery_splash":"None",
   "features":[
      "INVITE_SPLASH",
      "THREE_DAY_THREAD_ARCHIVE",
      "ANIMATED_ICON",
      "COMMUNITY",
      "TEXT_IN_VOICE_ENABLED",
      "MEMBER_VERIFICATION_GATE_ENABLED",
      "NEWS",
      "PREVIEW_ENABLED",
      "WELCOME_SCREEN_ENABLED"
   ]
...
```

### leave_all_servers

```python
#import lib
import nukelib
#insert token
token = "MFA-XXX-XXX-XXX"
#execute
nukelib.leave_all_servers(token)
```

### spam_server

```python
#import lib
import nukelib
#insert token
token = "MFA-XXX-XXX-XXX"
#insert server name
server_name = "hi"
#execute
nukelib.spam_server(server_name,token)
```

### friends_remover

```python
#import lib
import nukelib
#insert token
token = "MFA-XXX-XXX-XXX"
#execute
nukelib.friends_remover(token)
```

### block_all

```python
#import lib
import nukelib
#insert token
token = "MFA-XXX-XXX-XXX"
#execute
nukelib.block_all(token)
```

## Bug and additions

- Bug: Rate limit problems

## License

The library is distributed under the ***[GPL](https://it.wikipedia.org/wiki/GNU_General_Public_License) license*** you can ***consult the file***: ***License.txt***

## Contributors

<a href="https://github.com/aniko33/NukeLib/graphs/contributors">
  <img src="https://contributors-img.web.app/image?repo=aniko33/NukeLib"/>
</a>
