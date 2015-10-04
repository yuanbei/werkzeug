# -*- coding: utf-8 -*-
# noqa

STYLESHEET = r'''
body, input  { font-family: 'Lucida Grande', 'Lucida Sans Unicode',
               'Verdana', sans-serif; color: #000; text-align: center;
               margin: 1em; padding: 0; font-size: 15px; }
h1, h2, h3   { font-family: 'Lucida Grande', 'Lucida Sans Unicode',
               'Geneva', 'Verdana', sans-serif; font-weight: normal; }

input        { background-color: #fff; margin: 0; text-align: left;
               outline: none !important; }
input[type="submit"] { padding: 3px 6px; }
a            { color: #11557C; }
a:hover      { color: #177199; }
pre, code,
textarea     { font-family: 'Consolas', 'Monaco', 'Bitstream Vera Sans Mono',
               monospace; font-size: 14px; }

div.debugger { text-align: left; padding: 12px; margin: auto;
               background-color: white; }
h1           { font-size: 36px; margin: 0 0 0.3em 0; }
div.detail p { margin: 0 0 8px 13px; font-size: 14px; white-space: pre-wrap; }
div.explanation { margin: 20px 13px; font-size: 15px; color: #555; }
div.footer   { font-size: 13px; text-align: right; margin: 30px 0;
               color: #86989B; }

h2           { font-size: 16px; margin: 1.3em 0 0.0 0; padding: 9px;
               background-color: #11557C; color: white; }
h2 em, h3 em { font-style: normal; color: #A5D6D9; font-weight: normal; }

div.traceback, div.plain { border: 1px solid #ddd; margin: 0 0 1em 0;
                           padding: 10px; }
div.plain p      { margin: 0; }
div.plain textarea,
div.plain pre { margin: 10px 0 0 0; padding: 4px;
                background-color: #E8EFF0; border: 1px solid #D3E7E9; }
div.plain textarea { width: 99%; height: 300px; }
div.traceback h3 { font-size: 1em; margin: 0 0 0.8em 0; }
div.traceback ul { list-style: none; margin: 0; padding: 0 0 0 1em; }
div.traceback h4 { font-size: 13px; font-weight: normal; margin: 0.7em 0 0.1em 0; }
div.traceback pre { margin: 0; padding: 5px 0 3px 15px;
                    background-color: #E8EFF0; border: 1px solid #D3E7E9; }
div.traceback pre:hover { background-color: #DDECEE; color: black;
                          cursor: pointer; }
div.traceback div.source.expanded pre + pre { border-top: none; }

div.traceback span.ws { display: none; }
div.traceback pre.before, div.traceback pre.after {
    display: none; background: white;
}
div.traceback div.source.expanded pre.before,
div.traceback div.source.expanded pre.after {
    display: block;
}

div.traceback div.source.expanded span.ws {
    display: inline;
}

div.traceback blockquote { margin: 1em 0 0 0; padding: 0; }
div.traceback span.console-icon { float: right; padding: 2px;
                                  margin: -3px 2px 0 0; display: none; }
div.traceback span.console-icon:before {
    display: inline;
    content: "Console";
}
div.traceback span.console-icon:hover { background-color: #ddd; cursor: pointer;
                          border-color: #BFDDE0; }
div.traceback pre:hover span.console-icon { display: block; }
div.traceback cite.filename { font-style: normal; color: #3B666B; }

pre.console { border: 1px solid #ccc; background: white!important;
              color: black; padding: 5px!important;
              margin: 3px 0 0 0!important; cursor: default!important;
              max-height: 400px; overflow: auto; }
pre.console form { color: #555; }
pre.console input { background-color: transparent; color: #555;
                    width: 90%; font-family: 'Consolas', 'Deja Vu Sans Mono',
                    'Bitstream Vera Sans Mono', monospace; font-size: 14px;
                     border: none!important; }

span.string { color: #30799B; }
span.number { color: #9C1A1C; }
span.help   { color: #3A7734; }
span.object { color: #485F6E; }
span.extended { opacity: 0.5; }
span.extended:hover { opacity: 1; }
a.toggle { text-decoration: none; background-repeat: no-repeat;
           background-position: center center;
           background-image: url(?__debugger__=yes&cmd=resource&f=more.png); }
a.toggle:hover { background-color: #444; }
a.open { background-image: url(?__debugger__=yes&cmd=resource&f=less.png); }

pre.console div.traceback,
pre.console div.box { margin: 5px 10px; white-space: normal;
                      border: 1px solid #11557C; padding: 10px;
                      font-family: 'Lucida Grande', 'Lucida Sans Unicode', 'Geneva',
                      'Verdana', sans-serif;  }
pre.console div.box h3,
pre.console div.traceback h3 { margin: -10px -10px 10px -10px; padding: 5px;
                               background: #11557C; color: white; }

pre.console div.traceback pre:hover { cursor: default; background: #E8EFF0; }
pre.console div.traceback pre.syntaxerror {
    background: inherit;
    border: none;
    margin: 20px -10px -10px -10px;
    padding: 10px;
    border-top: 1px solid #BFDDE0;
    background: #E8EFF0;
}
pre.console div.noframe-traceback pre.syntaxerror {
    margin-top: -10px;
    border: none;
}

pre.console div.box pre.repr {
    padding: 0;
    margin: 0;
    background-color: white;
    border: none;
}
pre.console div.box table { margin-top: 6px; }
pre.console div.box pre { border: none; }
pre.console div.box pre.help { background-color: white; }
pre.console div.box pre.help:hover { cursor: default; }
pre.console table tr { vertical-align: top; }
div.console { border: 1px solid #ccc; padding: 4px; background-color: #fafafa; }

div.traceback pre, div.console pre {
    white-space: pre-wrap;       /* css-3 should we be so lucky... */
    white-space: -moz-pre-wrap;  /* Mozilla, since 1999 */
    white-space: -pre-wrap;      /* Opera 4-6 ?? */
    white-space: -o-pre-wrap;    /* Opera 7 ?? */
    word-wrap: break-word;       /* Internet Explorer 5.5+ */
    _white-space: pre;           /* IE only hack to re-specify in
                                 addition to word-wrap  */
}

div.pin-prompt {
    position: absolute;
    display: none;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background: rgba(255, 255, 255, 0.8);
}

div.pin-prompt .inner {
    background: #eee;
    padding: 10px 50px;
    width: 350px;
    margin: 10% auto 0 auto;
    border: 1px solid #ccc;
    border-radius: 2px;
}
'''

JAVASCRIPT = r'''
$(function() {
  if (!EVALEX_TRUSTED) {
    initPinBox();
  }

  /**
   * if we are in console mode, show the console.
   */
  if (CONSOLE_MODE && EVALEX) {
    openShell(null, $('div.console div.inner').empty(), 0);
  }

  $('div.traceback div.frame').each(function() {
    var
      target = $('pre', this),
      consoleNode = null,
      frameID = this.id.substring(6);

    target.click(function() {
      $(this).parent().toggleClass('expanded');
    });

    /**
     * Add an interactive console to the frames
     */
    if (EVALEX && target.is('.current')) {
      $('<span class="console-icon"></span>')
        .attr('title', 'Open an interactive python shell in this frame')
        .click(function() {
          consoleNode = openShell(consoleNode, target, frameID);
          return false;
        })
        .prependTo(target);
    }
  });

  /**
   * toggle traceback types on click.
   */
  $('h2.traceback').click(function() {
    $(this).next().slideToggle('fast');
    $('div.plain').slideToggle('fast');
  }).css('cursor', 'pointer');
  $('div.plain').hide();

  /**
   * Add extra info (this is here so that only users with JavaScript
   * enabled see it.)
   */
  $('span.nojavascript')
    .removeClass('nojavascript')
    .html('<p>To switch between the interactive traceback and the plaintext ' +
          'one, you can click on the "Traceback" headline.  From the text ' +
          'traceback you can also create a paste of it. ' + (!EVALEX ? '' :
          'For code execution mouse-over the frame you want to debug and ' +
          'click on the console icon on the right side.' +
          '<p>You can execute arbitrary Python code in the stack frames and ' +
          'there are some extra helpers available for introspection:' +
          '<ul><li><code>dump()</code> shows all variables in the frame' +
          '<li><code>dump(obj)</code> dumps all that\'s known about the ' +
          'object</ul>'));

  /**
   * Add the pastebin feature
   */
  $('div.plain form')
    .submit(function() {
      var label = $('input[type="submit"]', this);
      var old_val = label.val();
      label.val('submitting...');
      $.ajax({
        dataType:     'json',
        url:          document.location.pathname,
        data:         {__debugger__: 'yes', tb: TRACEBACK, cmd: 'paste',
                       s: SECRET},
        success:      function(data) {
          $('div.plain span.pastemessage')
            .removeClass('pastemessage')
            .text('Paste created: ')
            .append($('<a>#' + data.id + '</a>').attr('href', data.url));
        },
        error:        function() {
          alert('Error: Could not submit paste.  No network connection?');
          label.val(old_val);
        }
      });
      return false;
    });

  // if we have javascript we submit by ajax anyways, so no need for the
  // not scaling textarea.
  var plainTraceback = $('div.plain textarea');
  plainTraceback.replaceWith($('<pre>').text(plainTraceback.text()));
});

function initPinBox() {
  $('.pin-prompt form').submit(function(evt) {
    evt.preventDefault();
    var pin = this.pin.value;
    var btn = this.btn;
    btn.disabled = true;
    $.ajax({
      dataType: 'json',
      url: document.location.pathname,
      data: {__debugger__: 'yes', cmd: 'pinauth', pin: pin,
             s: SECRET},
      success: function(data) {
        btn.disabled = false;
        if (data.auth) {
          EVALEX_TRUSTED = true;
          $('.pin-prompt').fadeOut();
        } else {
          if (data.exhausted) {
            alert('Error: too many attempts.  Restart server to retry.');
          } else {
            alert('Error: incorrect pin');
          }
        }
        console.log(data);
      },
      error: function() {
        btn.disabled = false;
        alert('Error: Could not verify PIN.  Network error?');
      }
    });
  });
}

function promptForPin() {
  if (!EVALEX_TRUSTED) {
    $.ajax({
      url: document.location.pathname,
      data: {__debugger__: 'yes', cmd: 'printpin', s: SECRET}
    });
    $('.pin-prompt').fadeIn(function() {
      $('.pin-prompt input[name="pin"]').focus();
    });
  }
}


/**
 * Helper function for shell initialization
 */
function openShell(consoleNode, target, frameID) {
  promptForPin();
  if (consoleNode)
    return consoleNode.slideToggle('fast');
  consoleNode = $('<pre class="console">')
    .appendTo(target.parent())
    .hide()
  var historyPos = 0, history = [''];
  var output = $('<div class="output">[console ready]</div>')
    .appendTo(consoleNode);
  var form = $('<form>&gt;&gt;&gt; </form>')
    .submit(function() {
      var cmd = command.val();
      $.get('', {
          __debugger__: 'yes', cmd: cmd, frm: frameID, s: SECRET}, function(data) {
        var tmp = $('<div>').html(data);
        $('span.extended', tmp).each(function() {
          var hidden = $(this).wrap('<span>').hide();
          hidden
            .parent()
            .append($('<a href="#" class="toggle">&nbsp;&nbsp;</a>')
              .click(function() {
                hidden.toggle();
                $(this).toggleClass('open')
                return false;
              }));
        });
        output.append(tmp);
        command.focus();
        consoleNode.scrollTop(consoleNode.get(0).scrollHeight);
        var old = history.pop();
        history.push(cmd);
        if (typeof old != 'undefined')
          history.push(old);
        historyPos = history.length - 1;
      });
      command.val('');
      return false;
    }).
    appendTo(consoleNode);

  var command = $('<input type="text">')
    .appendTo(form)
    .keydown(function(e) {
      if (e.charCode == 100 && e.ctrlKey) {
        output.text('--- screen cleared ---');
        return false;
      }
      else if (e.charCode == 0 && (e.keyCode == 38 || e.keyCode == 40)) {
        if (e.keyCode == 38 && historyPos > 0)
          historyPos--;
        else if (e.keyCode == 40 && historyPos < history.length)
          historyPos++;
        command.val(history[historyPos]);
        return false;
      }
    });

  return consoleNode.slideDown('fast', function() {
    command.focus();
  });
}
'''


from werkzeug.debug._jquery import JQUERY

files = {
    'jquery.js': JQUERY,
    'debugger.js': JAVASCRIPT,
    'style.css': STYLESHEET,
}
