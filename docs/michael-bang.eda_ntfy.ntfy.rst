.. _mbang.eda_ntfy_source_plugin:

*******************
michael-bang.eda_ntfy.ntfy
*******************

**Listen for ntfy events**

.. contents::
    :local:
    :depth: 1

Synopsis
--------
- React to event received from ntfy

Requirements
------------
The below requirements are needed on the host that executes this module.

- python >= 3.6

Parameters
----------

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="3">Parameters</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>

        <tr>
            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>server</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">string</span>
                </div>
            </td>
            <td>
            </td>
            <td>
                <div>Name of the ntfy server to connect to.</div>
            </td>
        </tr>
        <tr>
            <td colspan="3">
                <div class="ansibleOptionAnchor" id="parameter-"></div>
                <b>topic</b>
                <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                <div style="font-size: small">
                    <span style="color: purple">string</span>
                </div>
            </td>
            <td>
            </td>
            <td>
                <div>Use to specify the name of the topic to subscribe to.</div>
            </td>
        </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - Although it is possible to specify and alternative server than ntfy.sh this has not been tested.

Examples
--------

.. code-block:: yaml

  - name: Listen for events from ntfy
    hosts: all
      sources:
        - michael-bang.eda_ntfy.ntfy:
            server: ntfy.sh
            topic: mytopic
    rules:
      - name: Print Add Events
        condition: event.payload.message == 'test'
        action:
          debug:
            msg: Message received 

Return Values
-------------

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
            <tr>
                <td colspan="2">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>payload</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>success</td>
                <td>
                            <div>A dictionary representing the JSON of the message received from ntfy</div>
                    <br/>
                </td>
            </tr>
    </table>
    <br/><br/>


        