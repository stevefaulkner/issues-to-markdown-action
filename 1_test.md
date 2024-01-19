# test

![image](https://github.com/stevefaulkner/test2b/assets/835859/97ddd50c-39fe-4bd5-b205-db855afd2ec9)

![test](https://github.com/stevefaulkner/test2b/blob/main/images/Screenshot%202024-01-19%20160350.png?raw=true")
---
subtitle: TetraLogical
title: VPATs/ACRs - Template wording for Remarks and Explanations cells
---

Copy and paste the relevant content into your accessibility conformance
report.

For more information, refer to [project ticket 241 on
GitHub](https://github.com/TetraLogical/Projects/issues/241).

Note that, for WCAG 2.0/2.1, this template only covers Level A & AA.

**[Note 1:]{.underline}** We don\'t need to include text for
\"Supports\" content (i.e. the related cell should be left blank). The
template does not mandate that text should be included - but, out there
in the wild, it\'s a bit inconsistent (some organizations include text,
others don\'t).

**[Note 2 (11^th^ Feb 2022):]{.underline}** The boilerplate text is
taken from the text used in the related success criterion. However, the
[official VPAT](https://www.itic.org/policy/accessibility/vpat) does not
specifically state you should use this language. Instead, it states:
"*When the conformance level is partially supports or does not support,
the remarks should identify the functions or features with issues
\[and\] how they do not fully support. If the criterion does not apply,
explain why. If an accessible alternative is used, describe it*".
Therefore, if you would prefer to use plainer language, feel free to do
so -- this text is purely for inspiration!

**Note 3 (25^th^ Feb 2023):** The document has been reorganised to group
Level A and Level AA, which makes it easier to follow along with the
document while completing an actual ACR (which also groups SCs by their
level).

# WCAG 2.0/2.1

## Level A

### 1.1.1 Non-text Content (Level A)

+-----------------------------------+-----------------------------------+
| **Supports**                      | Non-text content that is          |
|                                   | presented to the user has a text  |
|                                   | alternative that serves the       |
|                                   | equivalent purpose.               |
+===================================+===================================+
| **Partially supports**            | Non-text content that is          |
|                                   | presented to the user has a text  |
|                                   | alternative that serves the       |
|                                   | equivalent purpose, with some     |
|                                   | exceptions. These include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | Non-text content that is          |
|                                   | presented to the user mostly does |
|                                   | not have a text alternative that  |
|                                   | serves the equivalent purpose.    |
|                                   | Examples include:                 |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | The \[website/app/whatever\] does |
|                                   | not include non-text content.     |
+-----------------------------------+-----------------------------------+

### 1.2.1 Audio-only and Video-only (Prerecorded) (Level A)

+-----------------------------------+-----------------------------------+
| **Supports**                      | \[Delete/edit as appropriate\]    |
|                                   |                                   |
|                                   | An equivalent transcript is       |
|                                   | provided for all prerecorded      |
|                                   | audio-only content.               |
|                                   |                                   |
|                                   | An equivalent transcript is       |
|                                   | provided for all prerecorded      |
|                                   | video-only content.               |
|                                   |                                   |
|                                   | A separate audio track containing |
|                                   | equivalent information is         |
|                                   | provided for all prerecorded      |
|                                   | video-only content.               |
+===================================+===================================+
| **Partially supports**            | \[Delete/edit as appropriate\]    |
|                                   |                                   |
|                                   | An equivalent transcript is       |
|                                   | provided for all prerecorded      |
|                                   | audio-only content, with some     |
|                                   | exceptions. These include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
|                                   |                                   |
|                                   | An equivalent transcript is       |
|                                   | provided for all prerecorded      |
|                                   | video-only content, with some     |
|                                   | exceptions. These include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
|                                   |                                   |
|                                   | A separate audio track containing |
|                                   | equivalent information is         |
|                                   | provided for all prerecorded      |
|                                   | video-only content, with some     |
|                                   | exceptions. These include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | \[Delete/edit as appropriate\]    |
|                                   |                                   |
|                                   | Equivalent transcripts are not    |
|                                   | provided for prerecorded          |
|                                   | audio-only content. Examples      |
|                                   | include:                          |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
|                                   |                                   |
|                                   | Equivalent transcripts or         |
|                                   | separate audio tracks containing  |
|                                   | equivalent information are not    |
|                                   | provided for prerecorded          |
|                                   | video-only content. Examples      |
|                                   | include:                          |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | The \[website/app/whatever\] does |
|                                   | not include prerecorded           |
|                                   | audio-only or prerecorded         |
|                                   | video-only content.               |
+-----------------------------------+-----------------------------------+

### 1.2.2 Captions (Prerecorded) (Level A)

+-----------------------------------+-----------------------------------+
| **Supports**                      | Captions are provided for all     |
|                                   | prerecorded audio content within  |
|                                   | synchronized media.               |
+===================================+===================================+
| **Partially supports**            | Captions are provided for all     |
|                                   | prerecorded audio content within  |
|                                   | synchronized media, with some     |
|                                   | exceptions. These include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | Captions are not provided for     |
|                                   | prerecorded audio content within  |
|                                   | synchronized media. Examples      |
|                                   | include:                          |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | The \[website/app/whatever\] does |
|                                   | not include any prerecorded audio |
|                                   | content within synchronized       |
|                                   | media.                            |
+-----------------------------------+-----------------------------------+

### 1.2.3 Audio Description or Media Alternative (Prerecorded) (Level A)

+-----------------------------------+-----------------------------------+
| **Supports**                      | \[Delete/edit as appropriate\]    |
|                                   |                                   |
|                                   | An alternative for all time-based |
|                                   | media within synchronized media   |
|                                   | is provided.                      |
|                                   |                                   |
|                                   | An audio description for all      |
|                                   | prerecorded video content within  |
|                                   | synchronized media is provided.   |
+===================================+===================================+
| **Partially supports**            | \[Delete/edit as appropriate\]    |
|                                   |                                   |
|                                   | An alternative for all time-based |
|                                   | media within synchronized media   |
|                                   | is provided, with some            |
|                                   | exceptions. These include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
|                                   |                                   |
|                                   | An audio description for all      |
|                                   | prerecorded video content within  |
|                                   | synchronized media is provided,   |
|                                   | with some exceptions. These       |
|                                   | include:                          |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | \[Delete/edit as appropriate\]    |
|                                   |                                   |
|                                   | Alternatives for time-based media |
|                                   | within synchronized media are not |
|                                   | provided. Examples include:       |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
|                                   |                                   |
|                                   | Audio descriptions for            |
|                                   | prerecorded video content within  |
|                                   | synchronized media are not        |
|                                   | provided. Examples include:       |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | \[Edit/delete as appropriate\]    |
|                                   |                                   |
|                                   | The \[website/app/whatever\] does |
|                                   | not include any synchronized      |
|                                   | media that requires an accessible |
|                                   | alternative.                      |
|                                   |                                   |
|                                   | \[or\]                            |
|                                   |                                   |
|                                   | The \[website/app/whatever\]      |
|                                   | includes synchronized media, but  |
|                                   | they are media alternatives for   |
|                                   | text and are clearly labelled as  |
|                                   | such.                             |
+-----------------------------------+-----------------------------------+

### 1.3.1 Info and Relationships (Level A)

+-----------------------------------+-----------------------------------+
| **Supports**                      | All information, structure, and   |
|                                   | relationships conveyed through    |
|                                   | presentation can be               |
|                                   | programmatically determined or    |
|                                   | are available in text.            |
+===================================+===================================+
| **Partially supports**            | All information, structure, and   |
|                                   | relationships conveyed through    |
|                                   | presentation can be               |
|                                   | programmatically determined or    |
|                                   | are available in text, with some  |
|                                   | exceptions. These include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | Information, structure, and       |
|                                   | relationships conveyed through    |
|                                   | presentation cannot be            |
|                                   | programmatically determined and   |
|                                   | are not available in text.        |
|                                   | Examples include:                 |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | The \[website/app/whatever\] does |
|                                   | not include information,          |
|                                   | structure, or relationships       |
|                                   | conveyed through presentation.    |
+-----------------------------------+-----------------------------------+

### 1.3.2 Meaningful Sequence (Level A)

+-----------------------------------+-----------------------------------+
| **Supports**                      | A correct reading sequence can be |
|                                   | programmatically determined for   |
|                                   | all content.                      |
+===================================+===================================+
| **Partially supports**            | A correct reading sequence can be |
|                                   | programmatically determined for   |
|                                   | all content, with some            |
|                                   | exceptions. These include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | A correct reading sequence cannot |
|                                   | be programmatically determined    |
|                                   | for content, and therefore its    |
|                                   | meaning relies on its visual      |
|                                   | presentation alone. Examples      |
|                                   | include:                          |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | The sequence of content within    |
|                                   | the \[website/app/whatever\] does |
|                                   | not affect its meaning.           |
+-----------------------------------+-----------------------------------+

### 1.3.3 Sensory Characteristics (Level A)

+-----------------------------------+-----------------------------------+
| **Supports**                      | Instructions provided for         |
|                                   | understanding and operating       |
|                                   | content do not rely solely on     |
|                                   | sensory characteristics of        |
|                                   | components.                       |
+===================================+===================================+
| **Partially supports**            | Instructions provided for         |
|                                   | understanding and operating       |
|                                   | content do not rely solely on     |
|                                   | sensory characteristics of        |
|                                   | components, with some exceptions. |
|                                   | These include:                    |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | Instructions provided for         |
|                                   | understanding and operating       |
|                                   | content rely solely on sensory    |
|                                   | characteristics of components.    |
|                                   | Examples include:                 |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | The \[website/app/whatever\] does |
|                                   | not include instructions for      |
|                                   | understanding and operating       |
|                                   | content.                          |
+-----------------------------------+-----------------------------------+

### 1.4.1 Use of Color (Level A)

+-----------------------------------+-----------------------------------+
| **Supports**                      | Color is not used as the only     |
|                                   | visual means of conveying         |
|                                   | information, indicating an        |
|                                   | action, prompting a response, or  |
|                                   | distinguishing a visual element.  |
+===================================+===================================+
| **Partially supports**            | Color is not used as the only     |
|                                   | visual means of conveying         |
|                                   | information, indicating an        |
|                                   | action, prompting a response, or  |
|                                   | distinguishing a visual element,  |
|                                   | with some exceptions. These       |
|                                   | include:                          |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | Color is used as the only visual  |
|                                   | means of conveying information,   |
|                                   | indicating an action, prompting a |
|                                   | response, or distinguishing a     |
|                                   | visual element. Examples include: |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | *Very unlikely this will be the   |
|                                   | case.*                            |
+-----------------------------------+-----------------------------------+

### 1.4.2 Audio Control (Level A)

+-----------------------------------+-----------------------------------+
| **Supports**                      | \[Delete/edit as appropriate\]    |
|                                   |                                   |
|                                   | A mechanism is available to       |
|                                   | \[pause/stop/pause or stop\]      |
|                                   | audio on a \[Web page/screen\]    |
|                                   | that plays automatically for more |
|                                   | than 3 seconds \[and/or a         |
|                                   | mechanism is available to control |
|                                   | audio volume independently from   |
|                                   | the overall system volume         |
|                                   | level\].                          |
+===================================+===================================+
| **Partially supports**            | \[Delete/edit as appropriate\]    |
|                                   |                                   |
|                                   | A mechanism is available to       |
|                                   | \[pause/stop/pause or stop\]      |
|                                   | audio on a \[Web page/screen\]    |
|                                   | that plays automatically for more |
|                                   | than 3 seconds \[and/or a         |
|                                   | mechanism is available to control |
|                                   | audio volume independently from   |
|                                   | the overall system volume         |
|                                   | level\], with some exceptions.    |
|                                   | These include:                    |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | \[Delete/edit as appropriate\]    |
|                                   |                                   |
|                                   | No mechanism is available to      |
|                                   | pause or stop audio on a \[Web    |
|                                   | page/screen\] that plays          |
|                                   | automatically for more than 3     |
|                                   | seconds, and no mechanism is      |
|                                   | available to control the audio    |
|                                   | volume independently from the     |
|                                   | overall system volume level.      |
|                                   | Examples include:                 |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | The \[website/app/whatever\] does |
|                                   | not include audio that plays      |
|                                   | automatically for more than 3     |
|                                   | seconds.                          |
+-----------------------------------+-----------------------------------+

### 2.1.1 Keyboard (Level A)

+-----------------------------------+-----------------------------------+
| **Supports**                      | \[Delete as appropriate\]         |
|                                   |                                   |
|                                   | All functionality of the content  |
|                                   | is operable through a keyboard    |
|                                   | interface without requiring       |
|                                   | specific timings for individual   |
|                                   | keystrokes \[except where the     |
|                                   | underlying function requires      |
|                                   | input that depends on the path of |
|                                   | the user\'s movement and not just |
|                                   | the endpoints\].                  |
+===================================+===================================+
| **Partially supports**            | \[Delete as appropriate\]         |
|                                   |                                   |
|                                   | All functionality of the content  |
|                                   | is operable through a keyboard    |
|                                   | interface without requiring       |
|                                   | specific timings for individual   |
|                                   | keystrokes \[except where the     |
|                                   | underlying function requires      |
|                                   | input that depends on the path of |
|                                   | the user\'s movement and not just |
|                                   | the endpoints\], with some        |
|                                   | exceptions. These include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | \[Delete as appropriate\]         |
|                                   |                                   |
|                                   | Functionality of the content is   |
|                                   | not operable through a keyboard   |
|                                   | interface. Examples include:      |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
|                                   |                                   |
|                                   | Functionality of the content is   |
|                                   | operable through a keyboard       |
|                                   | interface, but it requires        |
|                                   | specific timings for individual   |
|                                   | keystrokes. Examples include:     |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | The \[website/app/whatever\] does |
|                                   | not include operable content.     |
+-----------------------------------+-----------------------------------+

### 2.1.2 No Keyboard Trap (Level A)

+-----------------------------------+-----------------------------------+
| **Supports**                      | \[Delete as appropriate\]         |
|                                   |                                   |
|                                   | For all components that receive   |
|                                   | keyboard focus, focus can be      |
|                                   | moved away from that component    |
|                                   | using the keyboard.               |
|                                   |                                   |
|                                   | Where non-standard methods are    |
|                                   | required to navigate away from a  |
|                                   | component, the user is advised of |
|                                   | this beforehand.                  |
+===================================+===================================+
| **Partially supports**            | \[Delete as appropriate\]         |
|                                   |                                   |
|                                   | For all components that receive   |
|                                   | keyboard focus, focus can be      |
|                                   | moved away from that component    |
|                                   | using the keyboard, with some     |
|                                   | exceptions. These include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
|                                   |                                   |
|                                   | Where non-standard methods are    |
|                                   | required to navigate away from a  |
|                                   | component, the user is advised of |
|                                   | this beforehand, with some        |
|                                   | exceptions. These include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | \[Delete as appropriate\]         |
|                                   |                                   |
|                                   | For all components that receive   |
|                                   | keyboard focus, focus cannot be   |
|                                   | moved away from that component    |
|                                   | using the keyboard. Examples      |
|                                   | include:                          |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
|                                   |                                   |
|                                   | Where non-standard methods are    |
|                                   | required to navigate away from a  |
|                                   | component, the user is not        |
|                                   | advised of this beforehand.       |
|                                   | Examples include:                 |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | The \[website/app/whatever\] does |
|                                   | not contain components that       |
|                                   | receive keyboard focus.           |
+-----------------------------------+-----------------------------------+

### 2.1.4 Character Key Shortcuts (Level A)

+-----------------------------------+-----------------------------------+
| **Supports**                      | The \[website/app/whatever\]      |
|                                   | includes keyboard shortcuts, but  |
|                                   | these shortcuts \[edit as         |
|                                   | appropriate\] can be turned off   |
|                                   | and/or remapped, or they are only |
|                                   | active when the related component |
|                                   | receives focus.                   |
+===================================+===================================+
| **Partially supports**            | The \[website/app/whatever\]      |
|                                   | includes keyboard shortcuts, but  |
|                                   | these shortcuts \[edit as         |
|                                   | appropriate\] can be turned off   |
|                                   | and/or remapped, or they are only |
|                                   | active when the related component |
|                                   | receives focus, with some         |
|                                   | exceptions. These include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | The \[website/app/whatever\]      |
|                                   | includes keyboard shortcuts that  |
|                                   | \[edit as appropriate\] cannot be |
|                                   | turned off, remapped, or can be   |
|                                   | activated even when the related   |
|                                   | component does not have focus.    |
|                                   | Examples include:                 |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | The \[website/app/whatever\] does |
|                                   | not use single character key      |
|                                   | keyboard shortcuts.               |
+-----------------------------------+-----------------------------------+

### 2.2.1 Timing Adjustable (Level A)

+-----------------------------------+-----------------------------------+
| **Supports**                      | \[Delete as appropriate\]         |
|                                   |                                   |
|                                   | The \[website/app/whatever\] has  |
|                                   | time limits, but these are        |
|                                   | \[required as part of a real-time |
|                                   | event / essential / set to a time |
|                                   | limit of longer than 20 hours.\]  |
|                                   |                                   |
|                                   | \[or\]                            |
|                                   |                                   |
|                                   | The \[website/app/whatever\] has  |
|                                   | time limits, but a mechanism is   |
|                                   | provided to \[turn off / adjust / |
|                                   | extend\] the time limit \[*if     |
|                                   | necessary, state where there is   |
|                                   | an option to turn                 |
|                                   | off/adjust/extend the time limit, |
|                                   | e.g. in the Settings menu*\].     |
+===================================+===================================+
| **Partially supports**            | \[Reword if necessary\]           |
|                                   |                                   |
|                                   | Mechanisms are provided to \[turn |
|                                   | off / adjust / extend\] time      |
|                                   | limits within the                 |
|                                   | \[website/app/whatever\], with    |
|                                   | some exceptions. These include:   |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | The \[website/app/whatever\] has  |
|                                   | time limits of less than 20 hours |
|                                   | which are not required as part of |
|                                   | a real-time event or otherwise    |
|                                   | essential, but there are no       |
|                                   | mechanisms available to \[turn    |
|                                   | off / adjust / extend\] time      |
|                                   | limits.                           |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | The \[website/app/whatever\] does |
|                                   | not have any time limits.         |
+-----------------------------------+-----------------------------------+

### 2.2.2 Pause, Stop, Hide (Level A)

+-----------------------------------+-----------------------------------+
| **Supports**                      | \[Edit/delete as necessary\]      |
|                                   |                                   |
|                                   | A mechanism is provided to pause, |
|                                   | stop, or hide all moving,         |
|                                   | blinking, and scrolling content,  |
|                                   | such as \[examples\].             |
|                                   |                                   |
|                                   | A mechanism is available to       |
|                                   | pause, stop, or hide all          |
|                                   | auto-updating information that    |
|                                   | starts automatically and is       |
|                                   | presented in parallel with other  |
|                                   | content, such as \[examples\].    |
+===================================+===================================+
| **Partially supports**            | \[Edit/delete as necessary\]      |
|                                   |                                   |
|                                   | A mechanism is provided to pause, |
|                                   | stop, or hide all moving,         |
|                                   | blinking, and scrolling content,  |
|                                   | with some exceptions. These       |
|                                   | include:                          |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
|                                   |                                   |
|                                   | A mechanism is available to       |
|                                   | pause, stop, or hide all          |
|                                   | auto-updating information that    |
|                                   | starts automatically and is       |
|                                   | presented in parallel with other  |
|                                   | content, with some exceptions.    |
|                                   | These include:                    |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | \[Edit/delete as necessary\]      |
|                                   |                                   |
|                                   | No mechanisms are provided to     |
|                                   | pause, stop, or hide all moving,  |
|                                   | blinking, and scrolling content.  |
|                                   | Examples include:                 |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
|                                   |                                   |
|                                   | No mechanisms are provided to     |
|                                   | pause, stop, or hide all          |
|                                   | auto-updating information that    |
|                                   | starts automatically and is       |
|                                   | presented in parallel with other  |
|                                   | content within the                |
|                                   | \[website/app/whatever\].         |
|                                   | Examples include:                 |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | The \[website/app/whatever\] does |
|                                   | not include any moving, blinking, |
|                                   | scrolling or auto-updating        |
|                                   | information (that starts          |
|                                   | automatically and is presented in |
|                                   | parallel with other content).     |
+-----------------------------------+-----------------------------------+

### 2.3.1 Three Flashes or Below Threshold (Level A)

+-----------------------------------+-----------------------------------+
| **Supports**                      | \[Delete as appropriate\]         |
|                                   |                                   |
|                                   | The \[website/app/whatever\] does |
|                                   | not include content that flashes. |
|                                   |                                   |
|                                   | The \[website/app/whatever\] does |
|                                   | not include content that flashes  |
|                                   | more than three times in any one  |
|                                   | second period.                    |
|                                   |                                   |
|                                   | The \[website/app/whatever\]      |
|                                   | includes content that flashes     |
|                                   | more than three seconds in any    |
|                                   | one second period, but the flash  |
|                                   | is below the [general flash and   |
|                                   | red flash                         |
|                                   | thresholds](https://              |
|                                   | www.w3.org/TR/WCAG21/#dfn-general |
|                                   | -flash-and-red-flash-thresholds). |
+===================================+===================================+
| **Partially supports**            | \[Delete as appropriate\]         |
|                                   |                                   |
|                                   | The \[website/app/whatever\] does |
|                                   | not include content that flashes  |
|                                   | more than three times in any one  |
|                                   | second period, with some          |
|                                   | exceptions. These include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
|                                   |                                   |
|                                   | The \[website/app/whatever\]      |
|                                   | includes content that flashes     |
|                                   | more than three seconds in any    |
|                                   | one second period, but the flash  |
|                                   | is below the [general flash and   |
|                                   | red flash                         |
|                                   | thresholds](https://              |
|                                   | www.w3.org/TR/WCAG21/#dfn-general |
|                                   | -flash-and-red-flash-thresholds), |
|                                   | with some exceptions. These       |
|                                   | include:                          |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | \[Delete as appropriate\]         |
|                                   |                                   |
|                                   | The \[website/app/whatever\]      |
|                                   | includes content that flashes     |
|                                   | more than three times in any one  |
|                                   | second period. Examples include:  |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
|                                   |                                   |
|                                   | The \[website/app/whatever\]      |
|                                   | includes content that flashes     |
|                                   | more than three seconds in any    |
|                                   | one second period, and the flash  |
|                                   | is above the [general flash and   |
|                                   | red flash                         |
|                                   | thresholds](https://              |
|                                   | www.w3.org/TR/WCAG21/#dfn-general |
|                                   | -flash-and-red-flash-thresholds). |
|                                   | Examples include:                 |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | *Very unlikely this will be the   |
|                                   | case.*                            |
+-----------------------------------+-----------------------------------+

### 2.4.1 Bypass Blocks (Level A)

+-----------------------------------+-----------------------------------+
| **Supports**                      | A mechanism is available to       |
|                                   | bypass blocks of content that are |
|                                   | repeated on multiple pages.       |
+===================================+===================================+
| **Partially supports**            | A mechanism is available to       |
|                                   | bypass blocks of content that are |
|                                   | repeated on multiple pages, with  |
|                                   | some exceptions. These include:   |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | A mechanism is not available to   |
|                                   | bypass blocks of content that are |
|                                   | repeated on multiple pages.       |
|                                   | Examples include:                 |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | \[Delete as appropriate\]         |
|                                   |                                   |
|                                   | The \[website/app/whatever\] does |
|                                   | not have blocks of content that   |
|                                   | are repeated on multiple pages.   |
|                                   |                                   |
|                                   | \[or\]                            |
|                                   |                                   |
|                                   | The application is a software     |
|                                   | product, and therefore this       |
|                                   | success criterion does not apply. |
+-----------------------------------+-----------------------------------+

### 2.4.2 Page Titled (Level A)

+-----------------------------------+-----------------------------------+
| **Supports**                      | All \[pages/screens/whatever\]    |
|                                   | have titles that describe their   |
|                                   | topic or purpose.                 |
+===================================+===================================+
| **Partially supports**            | All \[pages/screens/whatever\]    |
|                                   | have titles that describe their   |
|                                   | topic or purpose, with some       |
|                                   | exceptions. These include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | \[Pages/screens/whatever\] do not |
|                                   | have titles that describe their   |
|                                   | topic or purpose. Examples        |
|                                   | include:                          |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | The application is a software     |
|                                   | product, and therefore this       |
|                                   | success criterion does not apply. |
+-----------------------------------+-----------------------------------+

### 2.4.3 Focus Order (Level A)

+-----------------------------------+-----------------------------------+
| **Supports**                      | All focusable components receive  |
|                                   | focus in an order that preserves  |
|                                   | meaning and operability.          |
+===================================+===================================+
| **Partially supports**            | All focusable components receive  |
|                                   | focus in an order that preserves  |
|                                   | meaning and operability, with     |
|                                   | some exceptions. These include:   |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | Focusable components do not       |
|                                   | receive focus in an order that    |
|                                   | preserves meaning and             |
|                                   | operability. Examples include:    |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | The \[website/app/whatever\] does |
|                                   | not include any focusable         |
|                                   | components.                       |
+-----------------------------------+-----------------------------------+

### 2.4.4 Link Purpose (In Context) (Level A)

+-----------------------------------+-----------------------------------+
| **Supports**                      | The purpose of all links can be   |
|                                   | determined from the link text     |
|                                   | alone, or from the link text      |
|                                   | together with its                 |
|                                   | programmatically determined link  |
|                                   | context \[delete the following if |
|                                   | not required\] except where the   |
|                                   | purpose of the link is ambiguous  |
|                                   | to users in general.              |
+===================================+===================================+
| **Partially supports**            | The purpose of all links can be   |
|                                   | determined from the link text     |
|                                   | alone, or from the link text      |
|                                   | together with its                 |
|                                   | programmatically determined link  |
|                                   | context, with some exceptions.    |
|                                   | These include:                    |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | The purpose of all links cannot   |
|                                   | be determined from the link text  |
|                                   | alone, nor can the purpose be     |
|                                   | identified from the link text     |
|                                   | together with any                 |
|                                   | programmatically determined link  |
|                                   | context. Examples include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | The \[website/app/whatever\] does |
|                                   | not include any links.            |
+-----------------------------------+-----------------------------------+

### 2.5.1 Pointer Gestures (Level A)

+-----------------------------------+-----------------------------------+
| **Supports**                      | All functionality that uses       |
|                                   | \[delete as appropriate\]         |
|                                   | multipoint/path-based gestures    |
|                                   | for operation can also be         |
|                                   | operated with a single pointer    |
|                                   | without a path-based gesture      |
|                                   | \[delete the next part if         |
|                                   | appropriate\] unless a            |
|                                   | multipoint/path-based gesture is  |
|                                   | essential.                        |
+===================================+===================================+
| **Partially supports**            | All functionality that uses       |
|                                   | \[delete as appropriate\]         |
|                                   | multipoint/path-based gestures    |
|                                   | for operation can also be         |
|                                   | operated with a single pointer    |
|                                   | without a path-based gesture,     |
|                                   | with some exceptions. These       |
|                                   | include:                          |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | All functionality requires the    |
|                                   | use of \[delete as appropriate\]  |
|                                   | multipoint/path-based gestures,   |
|                                   | and cannot be operated using a    |
|                                   | single pointer. Examples include: |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | The                               |
|                                   | \[website/application/whatever\]  |
|                                   | does not require                  |
|                                   | multipoint/path-based gestures.   |
+-----------------------------------+-----------------------------------+

### 2.5.2 Pointer Cancellation (Level A)

+-----------------------------------+-----------------------------------+
| **Supports**                      | \[Delete/edit as required\]       |
|                                   |                                   |
|                                   | For all functionality that can be |
|                                   | operated using a single pointer,  |
|                                   | all pointer event interaction can |
|                                   | be cancelled as per the SC        |
|                                   | requirements.                     |
|                                   |                                   |
|                                   | \[or\]                            |
|                                   |                                   |
|                                   | For all functionality that can be |
|                                   | operated using a single pointer,  |
|                                   | the down-event of the pointer is  |
|                                   | not used to execute any part of   |
|                                   | the function.                     |
|                                   |                                   |
|                                   | For all functionality that can be |
|                                   | operated using a single pointer,  |
|                                   | completion of the function is on  |
|                                   | the up-event, and a mechanism is  |
|                                   | available to abort the function   |
|                                   | before completion/to undo the     |
|                                   | function after completion.        |
|                                   |                                   |
|                                   | For all functionality that can be |
|                                   | operated using a single pointer,  |
|                                   | the up-event reverses any outcome |
|                                   | of the preceding down-event.      |
|                                   |                                   |
|                                   | For all functionality that can be |
|                                   | operated using a single pointer,  |
|                                   | completing the function on the    |
|                                   | down-event is essential \[provide |
|                                   | examples\].                       |
+===================================+===================================+
| **Partially supports**            | \[Delete/edit as required\]       |
|                                   |                                   |
|                                   | For all functionality that can be |
|                                   | operated using a single pointer,  |
|                                   | all pointer event interaction can |
|                                   | be cancelled as per the SC        |
|                                   | requirements, with some           |
|                                   | exceptions. These include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
|                                   |                                   |
|                                   | \[or\]                            |
|                                   |                                   |
|                                   | For all functionality that can be |
|                                   | operated using a single pointer,  |
|                                   | the down-event of the pointer Is  |
|                                   | not used to execute any part of   |
|                                   | the function, with some           |
|                                   | exceptions. These include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
|                                   |                                   |
|                                   | For all functionality that can be |
|                                   | operated using a single pointer,  |
|                                   | completion of the function is on  |
|                                   | the up-event, and a mechanism is  |
|                                   | available to abort the function   |
|                                   | before completion/to undo the     |
|                                   | function after completion, with   |
|                                   | some exceptions. These include:   |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
|                                   |                                   |
|                                   | For all functionality that can be |
|                                   | operated using a single pointer,  |
|                                   | the up-event reverses any outcome |
|                                   | of the preceding down-event, with |
|                                   | some exceptions. These include:   |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | \[Delete/edit as required\]       |
|                                   |                                   |
|                                   | For all functionality that can be |
|                                   | operated using a single pointer,  |
|                                   | pointer event interactions cannot |
|                                   | be cancelled as per the SC        |
|                                   | requirements.                     |
|                                   |                                   |
|                                   | \[or\]                            |
|                                   |                                   |
|                                   | For all functionality that can be |
|                                   | operated using a single pointer,  |
|                                   | the down-event of the pointer is  |
|                                   | used to execute any part of the   |
|                                   | function. Examples include:       |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
|                                   |                                   |
|                                   | For all functionality that can be |
|                                   | operated using a single pointer,  |
|                                   | completion of the function is not |
|                                   | on the up-event, and a mechanism  |
|                                   | is not available to abort the     |
|                                   | function before completion/to     |
|                                   | undo the function after           |
|                                   | completion. Examples include:     |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
|                                   |                                   |
|                                   | For all functionality that can be |
|                                   | operated using a single pointer,  |
|                                   | the up-event does not reverse any |
|                                   | outcome of the preceding          |
|                                   | down-event. Examples include:     |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | The \[website/app/whatever\] does |
|                                   | not include functionality that    |
|                                   | can be operated using a single    |
|                                   | pointer.                          |
+-----------------------------------+-----------------------------------+

### 2.5.3 Label in Name (Level A)

+-----------------------------------+-----------------------------------+
| **Supports**                      | For all user interface components |
|                                   | with labels that include text or  |
|                                   | images of text, the accessible    |
|                                   | name of the component contains    |
|                                   | the text that is presented        |
|                                   | visually.                         |
+===================================+===================================+
| **Partially supports**            | For all user interface components |
|                                   | with labels that include text or  |
|                                   | images of text, the accessible    |
|                                   | name of the component contains    |
|                                   | the text that is presented        |
|                                   | visually, with some exceptions.   |
|                                   | These include:                    |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | For all user interface components |
|                                   | with labels that include text or  |
|                                   | images of text, the accessible    |
|                                   | name of the component does not    |
|                                   | contain the text that is          |
|                                   | presented visually. Examples      |
|                                   | include:                          |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | The \[website/app/whatever\] does |
|                                   | not include user interface        |
|                                   | components that have labels that  |
|                                   | include text or images of text.   |
+-----------------------------------+-----------------------------------+

### 2.5.4 Motion Actuation (Level A)

+-----------------------------------+-----------------------------------+
| **Supports**                      | \[Delete/edit as required\]       |
|                                   |                                   |
|                                   | All functionality that can be     |
|                                   | operated by device motion or user |
|                                   | motion can also be operated by    |
|                                   | user interface components and     |
|                                   | responding to the motion can be   |
|                                   | disabled to prevent accidental    |
|                                   | actuation.                        |
|                                   |                                   |
|                                   | \[or\]                            |
|                                   |                                   |
|                                   | The motion is used to operate     |
|                                   | functionality through an          |
|                                   | accessibility supported           |
|                                   | interface.                        |
+===================================+===================================+
| **Partially supports**            | All functionality that can be     |
|                                   | operated by device motion or user |
|                                   | motion can also be operated by    |
|                                   | user interface components and     |
|                                   | responding to the motion can be   |
|                                   | disabled to prevent accidental    |
|                                   | actuation, with some exceptions.  |
|                                   | These include:                    |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | \[Edit/delete as appropriate\]    |
|                                   |                                   |
|                                   | Functionality that can be         |
|                                   | operated by device motion or user |
|                                   | motion cannot also be operated by |
|                                   | user interface components and     |
|                                   | responding to the motion cannot   |
|                                   | be disabled to prevent accidental |
|                                   | actuation. Examples include:      |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | \[Edit/delete as appropriate\]    |
|                                   |                                   |
|                                   | The \[website/app/whatever\] does |
|                                   | not include functionality that    |
|                                   | can be operated by device motion  |
|                                   | or user motion.                   |
|                                   |                                   |
|                                   | \[or\]                            |
|                                   |                                   |
|                                   | The device motion or user motion  |
|                                   | is essential for the function and |
|                                   | removing it would invalidate the  |
|                                   | activity.                         |
+-----------------------------------+-----------------------------------+

### 3.1.1 Language of Page (Level A)

+-----------------------------------+-----------------------------------+
| **Supports**                      | The default language of all pages |
|                                   | can be programmatically           |
|                                   | determined.                       |
+===================================+===================================+
| **Partially supports**            | The default language of all pages |
|                                   | can be programmatically           |
|                                   | determined, with some exceptions. |
|                                   | These include:                    |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | The default language of pages     |
|                                   | cannot be programmatically        |
|                                   | determined.                       |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | It is not possible for developers |
|                                   | to programmatically specify the   |
|                                   | human language for native         |
|                                   | \[iOS/Android/whatever\]          |
|                                   | applications.                     |
+-----------------------------------+-----------------------------------+

### 3.2.1 On Focus (Level A)

+-----------------------------------+-----------------------------------+
| **Supports**                      | No user interface component       |
|                                   | initiates a change of context     |
|                                   | when it receives focus.           |
+===================================+===================================+
| **Partially supports**            | No user interface component       |
|                                   | initiates a change of context     |
|                                   | when it receives focus, with some |
|                                   | exceptions. These include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | User interface components         |
|                                   | initiate a change of content when |
|                                   | they receive focus. Examples      |
|                                   | include:                          |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | The \[website/app/whatever\] does |
|                                   | not include focusable user        |
|                                   | interface components.             |
+-----------------------------------+-----------------------------------+

### 3.2.2 On Input (Level A)

+-----------------------------------+-----------------------------------+
| **Supports**                      | \[Edit/delete as appropriate\]    |
|                                   |                                   |
|                                   | Changing the setting of user      |
|                                   | interface components does not     |
|                                   | automatically cause a change of   |
|                                   | context.                          |
|                                   |                                   |
|                                   | \[or\]                            |
|                                   |                                   |
|                                   | Although changing the setting of  |
|                                   | user interface components         |
|                                   | automatically causes a change of  |
|                                   | context, the user is advised of   |
|                                   | this behavior before using the    |
|                                   | component.                        |
+===================================+===================================+
| **Partially supports**            | \[Edit/delete as appropriate\]    |
|                                   |                                   |
|                                   | Changing the setting of user      |
|                                   | interface components does not     |
|                                   | automatically cause a change of   |
|                                   | context, with some exceptions.    |
|                                   | These include:                    |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
|                                   |                                   |
|                                   | \[or\]                            |
|                                   |                                   |
|                                   | Although changing the setting of  |
|                                   | user interface components         |
|                                   | automatically causes a change of  |
|                                   | context, the user is advised of   |
|                                   | this behavior before using the    |
|                                   | component, with some exceptions.  |
|                                   | These include:                    |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | Changing the setting of user      |
|                                   | interface components              |
|                                   | automatically causes a change of  |
|                                   | context, and the user is not      |
|                                   | advised of this behavior before   |
|                                   | using the component. Examples     |
|                                   | include:                          |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | The \[website/app/whatever\] does |
|                                   | not include user interface        |
|                                   | components that receive user      |
|                                   | input.                            |
+-----------------------------------+-----------------------------------+

### 3.3.1 Error Identification (Level A)

+-----------------------------------+-----------------------------------+
| **Supports**                      | For all input errors that are     |
|                                   | automatically detected, the item  |
|                                   | that is in error is identified    |
|                                   | and the error is described to the |
|                                   | user in text.                     |
+===================================+===================================+
| **Partially supports**            | For all input errors that are     |
|                                   | automatically detected, the item  |
|                                   | that is in error is identified    |
|                                   | and the error is described to the |
|                                   | user in text, with some           |
|                                   | exceptions. These include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | Input errors that are             |
|                                   | automatically detected are not    |
|                                   | identified and are not described  |
|                                   | to the user in text. Examples     |
|                                   | include:                          |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | The \[website/app/whatever\] does |
|                                   | not contain any components        |
|                                   | expecting user input that could   |
|                                   | lead to input errors.             |
+-----------------------------------+-----------------------------------+

### 3.3.2 Labels or Instructions (Level A)

+-----------------------------------+-----------------------------------+
| **Supports**                      | Labels or instructions are        |
|                                   | provided when content requires    |
|                                   | user input.                       |
+===================================+===================================+
| **Partially supports**            | Labels or instructions are        |
|                                   | provided when content requires    |
|                                   | user input, with some exceptions. |
|                                   | These include:                    |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | Labels or instructions are not    |
|                                   | provided when content requires    |
|                                   | user input. Examples include:     |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | The \[website/app/whatever\] does |
|                                   | not include content that requires |
|                                   | user input.                       |
+-----------------------------------+-----------------------------------+

### 4.1.1 Parsing (Level A)

+-----------------------------------+-----------------------------------+
| **Supports**                      | In all content implemented using  |
|                                   | markup languages, elements have   |
|                                   | complete start and end tags,      |
|                                   | elements are nested according to  |
|                                   | their specifications, elements do |
|                                   | not contain duplicate attributes, |
|                                   | and any IDs are unique, except    |
|                                   | where the specifications allow    |
|                                   | these features.                   |
+===================================+===================================+
| **Partially supports**            | In all content implemented using  |
|                                   | markup languages, elements have   |
|                                   | complete start and end tags,      |
|                                   | elements are nested according to  |
|                                   | their specifications, elements do |
|                                   | not contain duplicate attributes, |
|                                   | and any IDs are unique, except    |
|                                   | where the specifications allow    |
|                                   | these features, with some         |
|                                   | exceptions. These include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | \[Edit/delete as appropriate\]    |
|                                   |                                   |
|                                   | In all content implemented using  |
|                                   | markup languages, \[elements do   |
|                                   | not have complete start and end   |
|                                   | tags / elements are not nested    |
|                                   | according to their specifications |
|                                   | / elements contain duplicate      |
|                                   | attributes / IDs are not          |
|                                   | unique\]. Examples include:       |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | The \[app/software\] is not       |
|                                   | implemented using a markup        |
|                                   | language.                         |
+-----------------------------------+-----------------------------------+

### 4.1.2 Name, Role, Value (Level A)

+-----------------------------------+-----------------------------------+
| **Supports**                      | For all user interface            |
|                                   | components, the name and role can |
|                                   | be programmatically determined;   |
|                                   | states, properties, and values    |
|                                   | that can be set by the user can   |
|                                   | be programmatically set; and      |
|                                   | notification of changes to these  |
|                                   | items is available to user        |
|                                   | agents, including assistive       |
|                                   | technologies.                     |
+===================================+===================================+
| **Partially supports**            | For all user interface            |
|                                   | components, the name and role can |
|                                   | be programmatically determined;   |
|                                   | states, properties, and values    |
|                                   | that can be set by the user can   |
|                                   | be programmatically set; and      |
|                                   | notification of changes to these  |
|                                   | items is available to user        |
|                                   | agents, including assistive       |
|                                   | technologies, with some           |
|                                   | exceptions. These include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | \[Edit/delete as appropriate\]    |
|                                   |                                   |
|                                   | The name, role, or state of user  |
|                                   | interface components cannot be    |
|                                   | programmatically determined.      |
|                                   |                                   |
|                                   | The values of user interface      |
|                                   | components that can be set by the |
|                                   | user cannot be programmatically   |
|                                   | set.                              |
|                                   |                                   |
|                                   | Notification of changes to user   |
|                                   | interface components is not       |
|                                   | available to user agents,         |
|                                   | including assistive technologies. |
|                                   |                                   |
|                                   | Examples include:                 |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | The \[website/app/whatever\] does |
|                                   | not include user interface        |
|                                   | components.                       |
+-----------------------------------+-----------------------------------+

## Level AA

### 1.2.4 Captions (Live) (Level AA)

+-----------------------------------+-----------------------------------+
| **Supports**                      | Captions are provided for all     |
|                                   | live audio content within         |
|                                   | synchronized media.               |
+===================================+===================================+
| **Partially supports**            | Captions are provided for all     |
|                                   | live audio content within         |
|                                   | synchronized media, with some     |
|                                   | exceptions. These include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | Captions are not provided for     |
|                                   | live audio content within         |
|                                   | synchronized media. Examples      |
|                                   | include:                          |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | The \[website/app/whatever\] does |
|                                   | not include live audio content    |
|                                   | within synchronized media.        |
+-----------------------------------+-----------------------------------+

### 1.2.5 Audio Description (Prerecorded) (Level AA)

+-----------------------------------+-----------------------------------+
| **Supports**                      | Audio descriptions are provided   |
|                                   | for all prerecorded video content |
|                                   | within synchronized media.        |
+===================================+===================================+
| **Partially supports**            | Audio descriptions are provided   |
|                                   | for all prerecorded video content |
|                                   | within synchronized media, with   |
|                                   | some exceptions. These include:   |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | Audio descriptions are not        |
|                                   | provided for prerecorded video    |
|                                   | content within synchronized       |
|                                   | media. Examples include:          |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | The \[website/app/whatever\] does |
|                                   | not include prerecorded video     |
|                                   | content within synchronized       |
|                                   | media.                            |
+-----------------------------------+-----------------------------------+

### 1.3.4 Orientation (Level AA)

+-----------------------------------+-----------------------------------+
| **Supports**                      | The \[website/app/whatever\] does |
|                                   | not restrict the view and         |
|                                   | operation of content to a single  |
|                                   | display orientation \[except for  |
|                                   | \_*list of instances of exempted  |
|                                   | content and why it is exempt,     |
|                                   | e.g. a piano keyboard*\_\].       |
+===================================+===================================+
| **Partially supports**            | The \[website/app/whatever\] does |
|                                   | not restrict the view and         |
|                                   | operation of content to a single  |
|                                   | display orientation, with some    |
|                                   | exceptions. These include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | The \[website/app/whatever\]      |
|                                   | restricts the view and operation  |
|                                   | of content to                     |
|                                   | (\[portrait/landscape\]) display  |
|                                   | orientation. Examples include:    |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | *Very unlikely this will be the   |
|                                   | case, except possibly for PDFs.*  |
+-----------------------------------+-----------------------------------+

### 1.3.5 Identify Input Purpose (Level AA)

+-----------------------------------+-----------------------------------+
| **Supports**                      | The purpose of all input fields   |
|                                   | that collect information about    |
|                                   | the user can be programmatically  |
|                                   | determined.                       |
+===================================+===================================+
| **Partially supports**            | The purpose of all input fields   |
|                                   | that collect information about    |
|                                   | the user can be programmatically  |
|                                   | determined, with some exceptions. |
|                                   | These include:                    |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | The purpose of input fields that  |
|                                   | collect information about the     |
|                                   | user cannot be programmatically   |
|                                   | determined. Examples include:     |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | \[Delete as appropriate\]         |
|                                   |                                   |
|                                   | The \[website/app/whatever\] does |
|                                   | not include input fields that     |
|                                   | collect information about the     |
|                                   | user.                             |
|                                   |                                   |
|                                   | \[or\]                            |
|                                   |                                   |
|                                   | It is not possible for developers |
|                                   | to programmatically identify the  |
|                                   | purpose of input fields that      |
|                                   | collect information about the     |
|                                   | user within native                |
|                                   | \[iOS/Android/whatever\]          |
|                                   | applications.                     |
|                                   |                                   |
|                                   | \[or\]                            |
|                                   |                                   |
|                                   | The application is a software     |
|                                   | product, and therefore this       |
|                                   | success criterion does not apply. |
+-----------------------------------+-----------------------------------+

### 1.4.3 Contrast (Minimum) (Level AA)

+-----------------------------------+-----------------------------------+
| **Supports**                      | \[Delete/edit as appropriate\]    |
|                                   |                                   |
|                                   | The visual presentation of all    |
|                                   | text \[and all images of text\]   |
|                                   | has a contrast ratio of at least  |
|                                   | 4.5:1, \[while large-scale text   |
|                                   | and images of large-scale text    |
|                                   | have a contrast ratio of at least |
|                                   | 3:1\].                            |
+===================================+===================================+
| **Partially supports**            | \[Delete/edit as appropriate\]    |
|                                   |                                   |
|                                   | The visual presentation of all    |
|                                   | text \[and all images of text\]   |
|                                   | has a contrast ratio of at least  |
|                                   | 4.5:1, \[while large-scale text   |
|                                   | and images of large-scale text    |
|                                   | have a contrast ratio of at least |
|                                   | 3:1\], with some exceptions.      |
|                                   | These include:                    |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | \[Delete/edit as appropriate\]    |
|                                   |                                   |
|                                   | The visual presentation of text   |
|                                   | and images of text has a contrast |
|                                   | ratio of less than 4.5:1, \[while |
|                                   | large-scale text and images of    |
|                                   | large-scale text have a contrast  |
|                                   | ratio of less than 3:1\].         |
|                                   | Examples include:                 |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | *Very unlikely this will be the   |
|                                   | case, except in the case of       |
|                                   | documents, e.g. PDFs.*            |
+-----------------------------------+-----------------------------------+

### 1.4.4 Resize Text (Level AA)

+-----------------------------------+-----------------------------------+
| **Supports**                      | \[Delete/edit as appropriate\]    |
|                                   |                                   |
|                                   | \[Except for captions and images  |
|                                   | of text,\] all text can be        |
|                                   | resized without assistive         |
|                                   | technology by zooming up to 200%  |
|                                   | with no loss of content or        |
|                                   | functionality.                    |
+===================================+===================================+
| **Partially supports**            | \[Delete/edit as appropriate\]    |
|                                   |                                   |
|                                   | \[Except for captions and images  |
|                                   | of text,\] all text can be        |
|                                   | resized without assistive         |
|                                   | technology by zooming up to 200%  |
|                                   | with no loss of content or        |
|                                   | functionality, with some          |
|                                   | exceptions. These include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | \[Delete/edit as appropriate\]    |
|                                   |                                   |
|                                   | \[Except for captions and images  |
|                                   | of text,\] Resizing text by       |
|                                   | zooming up to 200% without        |
|                                   | assistive technology results in   |
|                                   | the loss of content \[and/or\]    |
|                                   | functionality. Examples include:  |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
|                                   |                                   |
|                                   | \[or\]                            |
|                                   |                                   |
|                                   | The \[website/app\] does not      |
|                                   | support text resizing based on    |
|                                   | the operating system settings,    |
|                                   | and does not provide any          |
|                                   | mechanism to resize text to 200%. |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | \[Delete/edit as appropriate\]    |
|                                   |                                   |
|                                   | The \[website/app/whatever\] does |
|                                   | not include any text content      |
|                                   | \[except for captions and/or      |
|                                   | images of text\].                 |
+-----------------------------------+-----------------------------------+

### 1.4.5 Images of Text (Level AA)

+-----------------------------------+-----------------------------------+
| **Supports**                      | \[Delete/edit as appropriate\]    |
|                                   |                                   |
|                                   | Text, rather than images of text, |
|                                   | is used to convey information     |
|                                   | \[except for \_*list of           |
|                                   | exceptions and why they are       |
|                                   | exceptions*\_\].                  |
+===================================+===================================+
| **Partially supports**            | \[Delete/edit as appropriate\]    |
|                                   |                                   |
|                                   | Text, rather than images of text, |
|                                   | is used to convey information     |
|                                   | \[except for \_*list of           |
|                                   | exceptions and why they are       |
|                                   | exceptions*\_\], with some        |
|                                   | exceptions. These include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | Images of text, rather than text, |
|                                   | are used to convey information.   |
|                                   | Examples include:                 |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | The \[website/app/whatever\] does |
|                                   | not include any text content.     |
+-----------------------------------+-----------------------------------+

### 1.4.10 Reflow (Level AA)

+-----------------------------------+-----------------------------------+
| **Supports**                      | \[Delete/edit as appropriate\]    |
|                                   |                                   |
|                                   | All content can be resized to a   |
|                                   | width of 320 CSS pixels/a height  |
|                                   | of 256 CSS pixels without loss of |
|                                   | content or functionality, and     |
|                                   | without requiring scrolling in    |
|                                   | two dimensions \[except for       |
|                                   | \_*content that is exempt from    |
|                                   | the requirement, e.g. maps,       |
|                                   | images, diagrams, video, data     |
|                                   | tables, presentations, etc.*\_\]. |
+===================================+===================================+
| **Partially supports**            | \[Delete/edit as appropriate\]    |
|                                   |                                   |
|                                   | All content can be resized to a   |
|                                   | width of 320 CSS pixels/a height  |
|                                   | of 256 CSS pixels without loss of |
|                                   | content or functionality, and     |
|                                   | without requiring scrolling in    |
|                                   | two dimensions \[except for       |
|                                   | \_*content that is exempt from    |
|                                   | the requirement, e.g. maps,       |
|                                   | images, diagrams, video, data     |
|                                   | tables, presentations, etc.*\_\]  |
|                                   | with some exceptions. These       |
|                                   | include:                          |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | Content cannot be resized to a    |
|                                   | width of 320 CSS pixels/a height  |
|                                   | of 256 CSS pixels without loss of |
|                                   | content or functionality, and     |
|                                   | without requiring scrolling in    |
|                                   | two dimensions. Examples include: |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | \[Delete/edit as appropriate\]    |
|                                   |                                   |
|                                   | The \[website/app/whatever\] only |
|                                   | includes content that cannot be   |
|                                   | reflowed without losing meaning   |
|                                   | \[e.g. graphics/videos/whole data |
|                                   | tables/toolbars\].                |
|                                   |                                   |
|                                   | \[or\]                            |
|                                   |                                   |
|                                   | The \[app/platform/whatever\] is  |
|                                   | used in an environment which      |
|                                   | \[does not support reflow when    |
|                                   | content is zoomed to 400%/does    |
|                                   | not support zooming to 400%\].    |
|                                   |                                   |
|                                   | \[or\]                            |
|                                   |                                   |
|                                   | The application is a software     |
|                                   | product, and therefore this       |
|                                   | success criterion does not apply. |
+-----------------------------------+-----------------------------------+

### 1.4.11 Non-text Contrast (Level AA)

+-----------------------------------+-----------------------------------+
| **Supports**                      | The visual presentation of all    |
|                                   | user interface components and     |
|                                   | other graphical objects (except   |
|                                   | for components whose appearance   |
|                                   | is determined by the              |
|                                   | \[browser/operating system/user   |
|                                   | agent\]) has a contrast ratio of  |
|                                   | at least 3:1.                     |
+===================================+===================================+
| **Partially supports**            | The visual presentation of all    |
|                                   | user interface components and     |
|                                   | other graphical objects (except   |
|                                   | for those whose appearance is     |
|                                   | determined by the                 |
|                                   | \[browser/operating system/other  |
|                                   | user agent\]) has a contrast      |
|                                   | ratio of at least 3:1, with some  |
|                                   | exceptions. These include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | The visual presentation of user   |
|                                   | interface components and other    |
|                                   | graphical objects (except for     |
|                                   | those whose appearance is         |
|                                   | determined by the                 |
|                                   | \[browser/operating system/other  |
|                                   | user agent\]) has a contrast      |
|                                   | ratio of less than 3:1. Examples  |
|                                   | include:                          |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | \[Delete as appropriate\]         |
|                                   |                                   |
|                                   | The \[website/app/whatever\] does |
|                                   | not include user interface        |
|                                   | components or graphical objects.  |
|                                   |                                   |
|                                   | \[or\]                            |
|                                   |                                   |
|                                   | The visual presentation of all    |
|                                   | user interface components \[and   |
|                                   | graphical objects\] within the    |
|                                   | \[website/app/whatever\] is       |
|                                   | determined by the \[browser/other |
|                                   | user agent\].                     |
+-----------------------------------+-----------------------------------+

### 1.4.12 Text Spacing (Level AA)

+-----------------------------------+-----------------------------------+
| **Supports**                      | The \[website/app/whatever\]      |
|                                   | allows for the changing of all    |
|                                   | relevant text style properties    |
|                                   | without loss of content or        |
|                                   | functionality.                    |
+===================================+===================================+
| **Partially supports**            | The \[website/app/whatever\]      |
|                                   | allows for the changing of all    |
|                                   | relevant text style properties    |
|                                   | without loss of content or        |
|                                   | functionality, with some          |
|                                   | exceptions. These include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | Changing relevant text style      |
|                                   | properties within the             |
|                                   | \[website/app/whatever\] causes   |
|                                   | loss of content or functionality. |
|                                   | Examples include:                 |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | While the \[app's/whatever's\]    |
|                                   | development framework allows      |
|                                   | developers to set multiple text   |
|                                   | style properties, including those |
|                                   | covered by this success           |
|                                   | criterion, these properties       |
|                                   | cannot be modified by the user in |
|                                   | the operating system's settings.  |
|                                   |                                   |
|                                   | \[or\]                            |
|                                   |                                   |
|                                   | The application is a software     |
|                                   | product, and therefore this       |
|                                   | success criterion does not apply. |
+-----------------------------------+-----------------------------------+

### 1.4.13 Content on Hover or Focus (Level AA)

+-----------------------------------+-----------------------------------+
| **Supports**                      | All additional content displayed  |
|                                   | on hover or focus is dismissable, |
|                                   | hoverable, and persistent.        |
+===================================+===================================+
| **Partially supports**            | Additional content displayed on   |
|                                   | hover or focus is dismissable,    |
|                                   | hoverable, and persistent, with   |
|                                   | some exceptions. These include:   |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | Additional content displayed on   |
|                                   | hover or focus is not \[edit as   |
|                                   | appropriate\] dismissable,        |
|                                   | hoverable, or persistent.         |
|                                   | Examples include:                 |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | The \[website/app/whatever\] does |
|                                   | not include additional content    |
|                                   | that is displayed on hover or     |
|                                   | focus.                            |
+-----------------------------------+-----------------------------------+

### 2.4.5 Multiple Ways (Level AA)

+-----------------------------------+-----------------------------------+
| **Supports**                      | More than one way is available to |
|                                   | locate web pages, \[delete this   |
|                                   | next part if necessary\] except   |
|                                   | for pages that are the result of, |
|                                   | or a step in, a process.          |
+===================================+===================================+
| **Partially supports**            | More than one way is available to |
|                                   | locate web pages, \[delete this   |
|                                   | next part if necessary\] except   |
|                                   | for pages that are the result of, |
|                                   | or a step in, a process, with     |
|                                   | some exceptions. These include:   |
|                                   |                                   |
|                                   | Example 1                         |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | There is only one way to locate   |
|                                   | web pages that are not the result |
|                                   | of, or a step in, a process.      |
|                                   | Examples include:                 |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | \[Delete as appropriate\]         |
|                                   |                                   |
|                                   | Due to the relatively small size  |
|                                   | and simplicity of the             |
|                                   | \[website/web app/whatever\],     |
|                                   | this success criterion is not     |
|                                   | applicable.                       |
|                                   |                                   |
|                                   | \[or\]                            |
|                                   |                                   |
|                                   | As the \[website/web              |
|                                   | app/whatever\] is entirely        |
|                                   | comprised of pages that are the   |
|                                   | result of, or a step in, a        |
|                                   | process, this success criterion   |
|                                   | is not applicable.                |
|                                   |                                   |
|                                   | \[or\]                            |
|                                   |                                   |
|                                   | The application is a software     |
|                                   | product, and therefore this       |
|                                   | success criterion does not apply. |
+-----------------------------------+-----------------------------------+

### 2.4.6 Headings and Labels (Level AA)

+-----------------------------------+-----------------------------------+
| **Supports**                      | All headings and labels           |
|                                   | appropriately describe the topic  |
|                                   | or purpose of their related       |
|                                   | content.                          |
+===================================+===================================+
| **Partially supports**            | All headings and labels           |
|                                   | appropriately describe the topic  |
|                                   | or purpose of their related       |
|                                   | content, with some exceptions.    |
|                                   | These include:                    |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | Headings and labels do not        |
|                                   | appropriately describe the topic  |
|                                   | or purpose of their related       |
|                                   | content. Examples include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | The                               |
|                                   | \[website/application/whatever\]  |
|                                   | does not include headings or      |
|                                   | labels.                           |
+-----------------------------------+-----------------------------------+

### 2.4.7 Focus Visible (Level AA)

+-----------------------------------+-----------------------------------+
| **Supports**                      | All keyboard operable user        |
|                                   | interface components include an   |
|                                   | indication of keyboard focus.     |
+===================================+===================================+
| **Partially supports**            | All keyboard operable user        |
|                                   | interface components include an   |
|                                   | indication of keyboard focus,     |
|                                   | with some exceptions. These       |
|                                   | include:                          |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | Keyboard operable user interface  |
|                                   | components do not include an      |
|                                   | indication of keyboard focus.     |
|                                   | Examples include:                 |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | The                               |
|                                   | \[website/application/whatever\]  |
|                                   | does not include keyboard         |
|                                   | operable user interface           |
|                                   | components.                       |
+-----------------------------------+-----------------------------------+

### 3.1.2 Language of Parts (Level AA)

+-----------------------------------+-----------------------------------+
| **Supports**                      | The human language of each        |
|                                   | passage or phrase in the content  |
|                                   | of all pages can be               |
|                                   | programmatically determined.      |
+===================================+===================================+
| **Partially supports**            | The human language of each        |
|                                   | passage or phrase in the content  |
|                                   | of all pages can be               |
|                                   | programmatically determined, with |
|                                   | some exceptions. These include:   |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | The human language of each        |
|                                   | passage or phrase in the content  |
|                                   | of pages cannot be                |
|                                   | programmatically determined.      |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | \[Edit/delete as appropriate\]    |
|                                   |                                   |
|                                   | It is not possible for developers |
|                                   | to programmatically specify the   |
|                                   | human language of passages or     |
|                                   | phrases in the content of native  |
|                                   | \[iOS/Android/whatever\]          |
|                                   | applications.                     |
|                                   |                                   |
|                                   | \[or\]                            |
|                                   |                                   |
|                                   | The \[app/whatever\] only         |
|                                   | includes \[delete as              |
|                                   | appropriate\] proper names,       |
|                                   | technical terms, or words of      |
|                                   | indeterminate language.           |
+-----------------------------------+-----------------------------------+

### 3.2.3 Consistent Navigation (Level AA)

+-----------------------------------+-----------------------------------+
| **Supports**                      | Navigational mechanisms that are  |
|                                   | repeated on multiple web pages    |
|                                   | within a set of web pages occur   |
|                                   | in the same relative order each   |
|                                   | time they are repeated \[delete   |
|                                   | as appropriate\] unless a change  |
|                                   | is initiated by a user.           |
+===================================+===================================+
| **Partially supports**            | Navigational mechanisms that are  |
|                                   | repeated on multiple web pages    |
|                                   | within a set of web pages occur   |
|                                   | in the same relative order each   |
|                                   | time they are repeated \[delete   |
|                                   | as appropriate\] unless a change  |
|                                   | is initiated by a user, with some |
|                                   | exceptions. These include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | Navigational mechanisms that are  |
|                                   | repeated on multiple web pages    |
|                                   | within a set of web pages do not  |
|                                   | occur in the same relative order  |
|                                   | each time they are repeated.      |
|                                   | Examples include:                 |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | \[Edit/delete as appropriate\]    |
|                                   |                                   |
|                                   | The \[website/app/whatever\] does |
|                                   | not include navigation mechanisms |
|                                   | that are repeated on multiple web |
|                                   | pages within a set of web pages.  |
|                                   |                                   |
|                                   | \[or\]                            |
|                                   |                                   |
|                                   | \[Product name\] is a software    |
|                                   | product, and therefore this       |
|                                   | success criterion does not apply. |
+-----------------------------------+-----------------------------------+

### 3.2.4 Consistent Identification (Level AA)

+-----------------------------------+-----------------------------------+
| **Supports**                      | All components that have the same |
|                                   | functionality within a set of web |
|                                   | pages are identified              |
|                                   | consistently.                     |
+===================================+===================================+
| **Partially supports**            | All components that have the same |
|                                   | functionality within a set of web |
|                                   | pages are identified              |
|                                   | consistently, with some           |
|                                   | exceptions. These include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | Components that have the same     |
|                                   | functionality within a set of web |
|                                   | pages are not identified          |
|                                   | consistently. Examples include:   |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | \[Edit/delete as appropriate\]    |
|                                   |                                   |
|                                   | The \[website/app/whatever\] does |
|                                   | not include components that have  |
|                                   | the same functionality within a   |
|                                   | set of web pages.                 |
|                                   |                                   |
|                                   | \[or\]                            |
|                                   |                                   |
|                                   | \[Product name\] is a software    |
|                                   | product, and therefore this       |
|                                   | success criterion does not apply. |
+-----------------------------------+-----------------------------------+

### 3.3.3 Error Suggestion (Level AA)

+-----------------------------------+-----------------------------------+
| **Supports**                      | For all automatically detected    |
|                                   | input errors where suggestions    |
|                                   | for correction are known, these   |
|                                   | suggestions are provided to the   |
|                                   | user \[unless doing so would      |
|                                   | jeopardize the security or        |
|                                   | purpose of the content\].         |
+===================================+===================================+
| **Partially supports**            | For all automatically detected    |
|                                   | input errors where suggestions    |
|                                   | for correction are known, these   |
|                                   | suggestions are provided to the   |
|                                   | user \[unless doing so would      |
|                                   | jeopardize the security or        |
|                                   | purpose of the content\], with    |
|                                   | some exceptions. These include:   |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | For all automatically detected    |
|                                   | input errors where suggestions    |
|                                   | for correction are known,         |
|                                   | suggestions are not provided to   |
|                                   | the user. Examples include:       |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | \[Edit/delete as required\]       |
|                                   |                                   |
|                                   | The \[website/app/whatever\] does |
|                                   | not include any components        |
|                                   | requiring user input that have    |
|                                   | known suggestions for correction. |
|                                   |                                   |
|                                   | \[or\]                            |
|                                   |                                   |
|                                   | For all input errors that are     |
|                                   | automatically detected,           |
|                                   | suggestions for correction are    |
|                                   | known, but providing them would   |
|                                   | jeopardize the security or        |
|                                   | purpose of the content. For       |
|                                   | example \[examples\].             |
+-----------------------------------+-----------------------------------+

### 3.3.4 Error Prevention (Legal, Financial, Data) (Level AA)

+-----------------------------------+-----------------------------------+
| **Supports**                      | \[Edit/delete as appropriate\]    |
|                                   |                                   |
|                                   | Pages that \[cause legal          |
|                                   | commitments or financial          |
|                                   | transactions for the user to      |
|                                   | occur / modify or delete          |
|                                   | user-controllable data in data    |
|                                   | storage systems / submit user     |
|                                   | test responses\] are \[reversable |
|                                   | / checked for input errors and    |
|                                   | subsequently correctable /        |
|                                   | confirmable through a mechanism   |
|                                   | for reviewing, confirming, and    |
|                                   | correcting before finalizing the  |
|                                   | submission\].                     |
+===================================+===================================+
| **Partially supports**            | \[Edit/delete as appropriate\]    |
|                                   |                                   |
|                                   | Pages that \[cause legal          |
|                                   | commitments or financial          |
|                                   | transactions for the user to      |
|                                   | occur / modify or delete          |
|                                   | user-controllable data in data    |
|                                   | storage systems / submit user     |
|                                   | test responses\] are \[reversable |
|                                   | / checked for input errors and    |
|                                   | subsequently correctable /        |
|                                   | confirmable through a mechanism   |
|                                   | for reviewing, confirming, and    |
|                                   | correcting before finalizing the  |
|                                   | submission\], with some           |
|                                   | exceptions. These include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | Pages that \[cause legal          |
|                                   | commitments or financial          |
|                                   | transactions for the user to      |
|                                   | occur / modify or delete          |
|                                   | user-controllable data in data    |
|                                   | storage systems / submit user     |
|                                   | test responses\] are not          |
|                                   | \[reversable / checked for input  |
|                                   | errors and subsequently           |
|                                   | correctable / confirmable through |
|                                   | a mechanism for reviewing,        |
|                                   | confirming, and correcting before |
|                                   | finalizing the submission\].      |
|                                   | Examples include:                 |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | The \[website/app/whatever\] does |
|                                   | not include pages that cause      |
|                                   | legal commitments or financial    |
|                                   | transactions for the user to      |
|                                   | occur, modify or delete           |
|                                   | user-controllable data in data    |
|                                   | storage systems, or submit user   |
|                                   | test responses.                   |
+-----------------------------------+-----------------------------------+

### 4.1.3 Status Messages (Level AA)

+-----------------------------------+-----------------------------------+
| **Supports**                      | In all content implemented using  |
|                                   | markup languages, status messages |
|                                   | can be programmatically           |
|                                   | determined through role or        |
|                                   | properties such that they can be  |
|                                   | presented to the user by          |
|                                   | assistive technologies without    |
|                                   | receiving focus.                  |
+===================================+===================================+
| **Partially supports**            | In all content implemented using  |
|                                   | markup languages, status messages |
|                                   | can be programmatically           |
|                                   | determined through role or        |
|                                   | properties such that they can be  |
|                                   | presented to the user by          |
|                                   | assistive technologies without    |
|                                   | receiving focus, with some        |
|                                   | exceptions. These include:        |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Does not support**              | In all content implemented using  |
|                                   | markup languages, status messages |
|                                   | cannot be programmatically        |
|                                   | determined through role or        |
|                                   | properties such that they can be  |
|                                   | presented to the user by          |
|                                   | assistive technologies without    |
|                                   | receiving focus. Examples         |
|                                   | include:                          |
|                                   |                                   |
|                                   | -   Example 1                     |
|                                   |                                   |
|                                   | -   Example 2                     |
|                                   |                                   |
|                                   | -   Example 3                     |
+-----------------------------------+-----------------------------------+
| **Not applicable**                | \[Edit/delete as required\]       |
|                                   |                                   |
|                                   | The \[app/software/whatever\] is  |
|                                   | not implemented using a markup    |
|                                   | language.                         |
|                                   |                                   |
|                                   | \[or\]                            |
|                                   |                                   |
|                                   | The \[website/app/whatever\] does |
|                                   | not include status messages.      |
|                                   |                                   |
|                                   | \[or\]                            |
|                                   |                                   |
|                                   | The application is a software     |
|                                   | product, and therefore this       |
|                                   | success criterion does not apply. |
+-----------------------------------+-----------------------------------+
