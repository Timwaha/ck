MetricsReloaded
===============

Automated code metrics plugin for IntelliJ IDEA. You can find a nice
description of MetricsReloaded on [the IntelliJ IDEA Blog][1].

Getting started
---------------

Select the *Calculate Metrics...* menu item in the *Analyze* menu. Try the
*Lines of code metrics* profile first, if you haven't used MetricsReloaded
before.

Command line
------------

Metrics can also be calculated from the command line, for integration into
build servers. The results are saved into the specified xml file for later
analysis. Enter `idea metrics -h` on the terminal for help. Make sure
IntelliJ IDEA is not running when you try to invoke MetricsReloaded from the
terminal or it will not work. For a truly headless experience add the option
`-Djava.awt.headless=true` to the `idea.vmoptions` file in the `bin`
directory of the IntelliJ IDEA installation you are using on the build server.

Installation
------------

Find and install MetricsReloaded from IntelliJ IDEA's plugin manager.
Alternatively you can download [the zip file][2] manually and unpack it in
IntelliJ IDEA's plugin directory.



[1]: http://blog.jetbrains.com/idea/2014/09/touring-plugins-issue-1/
[2]: http://plugins.jetbrains.com/plugin/93
