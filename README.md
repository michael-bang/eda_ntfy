# Event-Driven Ansible

A simple source plugin for Event Driven Ansible that listens for events from ntfy (https://ntfy.sh/)

## Usage

The following is an example of how to use the ntfy Event Source Plugin within an Ansible Rulebook:

```yaml
- name: Listen for events from ntfy
  hosts: all
  sources:
    - michael_bang.eda_ntfy.ntfy:
        server: ntfy.sh
        topic: mytopic
  rules:
    - name: Print Add Events
      condition: event.payload.message == 'test'
      action:
        debug:
          msg: Message received 

```

It is possible to use a specific ntfy server eg. your own installed ntfy server. The code has currently only been tested against the external ntfy.sh so there might be issues.

Remember to set your topic in the topic variable to get the events from your topic

## License

Apache 2.0