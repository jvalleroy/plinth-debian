# Change Log
All notable changes to this project will be documented in this file.

## [0.15.3] - 2017-10-20
### Changed
- Rename Disks to Storage.
- Rename Snapshot to Storage Snapshots.
- Update Django version to 1.11.
- tt-rss: Enable API access by default.
- users: Migrate ldap bash script into actions/users.
- Allow access to plinth from outside the LAN.
- matrixsynapse: Disable public registration by default.
- power: Merge actions into the user dropdown.

### Added
- Add locales for Kannada (kn) and for Bengali (bn).
- ejabberd: Use Let's Encrypt certificate, also across renewals.
- matrix-synapse: Add enable/disable public registrations.
- networks: Move initial connection setup to Plinth.
- Move Avahi files from freedombox-setup.
- apache: Move freedombox.conf configuration to Plinth.
- Add generic framework for user group per application.
- networks: Activate the newly created connections.
- Add django-simple-captcha in the login page.
- captcha: Add flite tts for accessibility.
- sso: Add django-axes to project.
- sso: Add captcha validation on 3 failed attempts.
- matrixsynapse: Enable LDAP integration.
- letsencrypt: Automatically obtain and revoke SSL certificates.
- ci: Add circle-ci config to Plinth.

### Removed
- Remove creation of first-run.d directory.
- setup: Remove freedombox-setup related scripts.

### Fixed
- i18n, msgfmt: Flag percent symbol in ugettext.
- Fix front page label names.
- Fix vertical alignment of shortcut icons.
- Fix some Django deprecations.
- storage: Fix issue with locales that use other decimal separators.
- users: Restart nscd after setup.
- networks: Make setup script idempotent.
- ttrss: Make tt-rss api accessible using Apache basic auth.
- setup: Fix Plinth startup issues.
- storage: Simplified use of df to get disk information.
- Use gir1.2-nm-1.0 instead of gir1.2-networkmanager-1.0.
- Ensure url is a str for commonprefix.
- users: Fix creating a group.
- travis: Install configobj from Debian.
- letsencrypt: Handle case where current domain is empty.
- Handle both admin and non-admin user names in update user template.

## [0.15.2] - 2017-09-24
### Added
- letsencrypt: Show more info on cert validity status.
- letsencrypt: Add option to delete certificates.
- letsencrypt: Add option to let Plinth manage certbot's renewal hooks.
- power: Warn if a package manager is running before shutdown/restart.
- security: Install and manage fail2ban.
- names: Include domain and services from dynamicdns.
- Add contributing guidelines.
- disks: Add low disk space warning to system and disks page.
- Capture and log all Python warnings.
- ssh: New application to manage SSH server.
- apache: New module to manage Apache configuration.
- Add api module to get enabled services and access info.
- Add Django password validators.
- ejabberd, ikiwiki, ttrss: Add user login descriptions.

### Removed
- diaspora: Disable for this release due to issues affecting package.
- Remove help from navbar before firstboot complete.
- Remove print statement from tests.
- firewall: Remove redundant setup steps.
- first-run: Skip installation of essential modules from Plinth.

### Fixed
- i18n: Don't use backslash-newline for wrapping long lines.
- radicale: Update link to documentation.
- travis: Fix build errors due to change to non-system python.
- sso: Add check to see if auth-pubtkt module is available.
- sso: Upgrade crypto to 4096-bit RSA and SHA-512.
- sso, repro: Add safety checks to make sure auth_pubtkt is enabled.
- tahoe: Correct LAFS to Tahoe-LAFS in apps page.
- Users: Allow non-admin users to log out.

### Changed
- letsencrypt: Make Let's Encrypt an essential module.
- Update requirements list.
- Remove disabled apps as part of install.
- UI: Make apps and configure pages responsive on small screens.
- Make help accessible for logged-in non-admin users.
- sso: Use Login and Logout view classes instead of methods.
- Separate out the short description and app name.
- users: Move ldap structure config into normal setup.
- Don't run Plinth setup as part of freedombox/setup.
- firewall: Move remaining setup steps to Plinth.
- Move CI notifications to new channel.

## [0.15.1] - 2017-07-02
### Fixed
- Fixed python format string in translation.

## [0.15.0] - 2017-07-01
### Added
- Added Tahoe-LAFS module for distributed file storage.
- Added Diaspora* module for federated social networking.
- New Locales for Czech (cs) and Tamil (ta).
- Cache whether user is admin in context_processor.
- Introduced a new stylesheet to hold custom responsive css.
- ejabberd: Added option to enable/disable Message Archive Management.
- help: Added Debian release to about page.
- Added SSO using auth_pubtkt for Syncthing, Repro, and TT-RSS.
- SSO: Generate keys during plinth startup.

### Removed
- doc: Removed unused images.
- owncloud: Removed module, since it is no longer in Debian.
- apps, system: Removed modules, and merged into main.
- firstboot: Erased network graph and warning on WiFi passwords.
- Removed Power from config menu, since power drop-down was added.

### Changed
- datetime: Use timedatectl to get list of time zones.
- datetime: Rewrote action timezone-change in Python.
- Split reserved usernames list among modules.
- module_loader: Split the URLs inclusion step.
- menu: Lazily reverse menu item URLs.
- firstboot: de-bloat first welcome screen.
- Pinned footer to the bottom of the viewport.
- disks: restrict precision of reported available space on root partition.
- diagnostics: Disable button if app/service is not running.
- help: only show help pages if user is logged in.
- navbar: moved logout to user drop-down and added a new power drop-down.
- letsencrypt: directly call certbot in action script.

### Fixed
- disks: Show disabled partition resize option if no space is available.
- actions: Make subparsers mandatory, fixes calls without arguments.
- networks: Fix failing network test.
- Added line break to titles for frontpage shortcuts.
- syncthing: Fixed typos and clarity in description.
- firewall: Fix 500 error when firewalld is not running.
- setup: Disable install/upgrade when dpkg/apt is running.
- utils: Fix test case failures due to caching.
- disks: Use information from lsblk for more accuracy.
- datetime: Show timezone properly when it not in expected list.
- disks: add missing import json.
- licenses: correct info for ejabberd.
- disks: delete existing test file, if necessary.

## [0.14.0] - 2017-04-09
### Added
- tor: Added option to use upstream bridges.
- openvpn: Added to front page.
- openvpn: Non-admin users can download their own profiles.
- Added Debian badges to README.
- Added new locales for Hindi (hi) and Gujarati (gu).
- Added syncthing module for file synchronization.
- Added Matrix Synapse as chat server with groups, audio and video.

### Removed
- Removed use of stronghold whitelisting, no longer necessary.
- Removed unused symlink to doc directory.

### Changed
- Require admin access for all system configuration pages.
- Change appearance of topbar and footer.
- Use common LDAP auth apache configuration in all modules.

### Fixed
- Added missing shaarli logo.
- Overwrite existing doc and static folders when installing.
- Added line break to infinoted title, used by front page shortcut.
- Fixed URL in INSTALL doc.
- openvpn: Regenerate user key or certificate if empty.
- openvpn: Prevent failures when regenerating user certificate.
- Fixed augeas error in travis build.
- disks: Workaround issue in parted during resize.

## [0.13.1] - 2017-01-22
### Added
- Added new locale for Japanese (ja).

### Fixed
- setup: Fixed an infinite redirect in a rare case.
- Fixed URLs referencing jsxc JS and CSS files.
- setup.py: Install all first-run scripts for freedombox-setup.
- ikiwiki: Fixed showing icon for newly created wiki/blog.

## [0.13.0] - 2017-01-18
### Added
- Added command line argument --list-modules which will list modules
  and exit. It can be followed by "essential" or "optional" to only
  list those modules.
- Added JS license web labels for LibreJS.
- Added basic configuration form for Minetest server.
- Added Domain Name Server (BIND) module.
- help: Added indicator for new plinth version available.
- Added Gobby Server (infinoted) module.

### Changed
- frontpage: Show app logos instead of generic icons.
- Prevent anonymous users from accessing setup pages.
- Firstboot, KVStore: merge old firstboot state fields.
- tor: Use Plinth-specific instance instead of default.
- xmpp: Split into ejabberd and jsxc modules.
- users: Moved part of LDAP setup to first-run.

## [0.12.0] - 2016-12-08
### Added
- Added screenshots to Readme.
- repro: Open up RTP ports.
- Allow modules to register steps for first_boot.
- frontpage: Show Configure button in service details, when user is logged in.
- minetest: Add mods packages to be installed with server.
- networks: Support configuring IPv6 networks.

### Fixed
- Upstream patch from Debian bug #837206 to fix DB and log file
  permissions. Also switch to new setup command.
- Include module static files in build, required for Debian package build.
- dynamicdns: Allow reading status as non-root.
- config: Set current domainname again after hostname change.
- config: Handle clearing of domain name.
- letsencrypt: When no domains are configured, show better message,
  and hide diagnostics button.
- frontpage: Fix shortcut spacing issue.
- xmpp: Updated to work with JSXC 3.0.0.

### Changed
- repro: Use firewalld provided SIP services.
- xmpp: Show more clearly if domain is not set.
- frontpage: Don't show apps requiring login, unless logged in.
- ttrss: Show status block.
- frontpage: Make app icons larger.
- frontpage: Center shortcut text under icons.
- frontpage: Move info to bottom and center.
- firewall: Only show services that have completed setup.
- firewall: Collapse port lists so they are hidden by default.
- users: Make it harder to accidentally delete the only Plinth user.

## [0.11.0] - 2016-09-21
### Added
- Added loading icon for other busy operations.
- Added basic front page with shortcuts to web apps, and information
  about enabled services.
- Allow initial setup operation to happen without package
  installation.
- networks: Add polkit rules for network management.
- Update man page to add setup operations.
- Add argument to list packages needed by apps.
- networks: Add batctl as dependency.

### Fixed
- users: Fixed checking restricted usernames.
- users: Display error message if unable to set SSH keys.
- help: Minor updates and fixes to status log.
- Updated translations to fix weblate errors.
- Fixed spelling errors in datetime and letsencrypt modules.
- users: Flush nscd cache after user operations.
- monkeysphere: Adopted to using SHA256 fingerprints.
- monkeysphere: Sort items for consistent display.
- monkeysphere: Handle new uid format of gpg2.
- monkeysphere: Fixed handling of unavailable imported domains.
- minetest: Fixed showing status block and diagnostics.
- Fix stretched favicon.

### Changed
- dynamicdns, monkeysphere, transmission, upgrades: Use actions where
  root is required, so that Plinth can run as non-root.
- xmpp: Switched to using ruamel.yaml to modify ejabberd config.
- Exit with error if any of the setup steps fail.
- actions: Hush some unneeded output of systemd.
- letsencrypt: Depend on the new certbot package.
- Switch base template from container-fluid to container. This will
  narrow the content area for larger displays.
- Readjust the responsive widths of various tables.
- Print django migrate messages only in debug.
- Tune log message verbosity.
- Plinth no longer runs as root user.  Fix all applications that were
  requiring root permission.
- xmpp: Replace jwchat with jsxc. Bump module version number so
  current installs can be updated.
- ikiwiki: Allow only alphanumerics in wiki/blog name.

### Removed
- Remove width management for forms.

## [0.10.0] - 2016-08-12
### Added
- Added Disks module to show free space of mounted partitions and
  allow expanding the root partition.
- Added Persian (fa) locale.
- Added Indonesian (id) locale.
- Added options to toggle Tor relay and bridge relay modes.
- Added Security module to control login restrictions.
- Added a page to display recent status log from Plinth. It is
  accessible from the 500 error page.
- networks: Added ability to configure generic interfaces.
- networks: Added 'disabled' IPv4 method.
- networks: Added configuration of wireless BSSID, band, and channel.
- networks: Added NetworkManager dispatcher script to configure
  batman-adv mesh networking.
- radicale: Added access rights control.
- tor: Added spinner when configuration process is ongoing.
- Allowed --setup command to take a list of modules to setup.
- Added Vagrantfile.
- Added Snapshots module to manage Btrfs snapshots.

### Removed
- networks: Removed hack for IP address fetching.

### Fixed
- Improved Dynamic DNS status message when no update needed.
- Improved Ikiwiki description.
- Added check if a2query is installed before using it, since apache2
  is not a dependency for Plinth.
- networks: Fixed incorrect access for retrieving DNS entries.
- Fixed issue with lost menus in Django 1.10.
- Added workaround for script prefix problem in stronghold.
- users: Fixed editing users without SSH keys.

### Changed
- Added suggested packages for ikiwiki. Removed recommends since they
  are installed automatically.
- users: Switched to using dpkg-reconfigure to configure several
  packages. This will work even if the package is already installed.
- Bumped required version of Django to 1.10.

## [0.9.4] - 2016-06-14
### Fixed
- Fixed quoted values in nslcd config.

## [0.9.3] - 2016-06-12
### Added
- Added Polish translation.
- Added check to Diagnostics to skip tests for modules that have not
  been setup.
- Added sorting of menu items per locale.
- Allowed setting IP for shared network connections.

### Fixed
- Fixed issue preventing access to Plinth on a non-standard port.
- Fixed issue in Privoxy configuration. Two overlapping
  listen-addresses were configured, which prevented privoxy service
  from starting.
- Fixed issues with some diagnostic tests that would show false
  positive results.
- Fixed some username checks that could cause errors when editing the
  user.
- Switched to using apt-get for module setup in Plinth. This fixes
  several issues that were seen during package installs.

### Changed
- Moved Dynamic DNS and Pagekite from Applications to System
  Configuration.

### Deprecated
- Dealt with ownCloud removal from Debian. The ownCloud page in Plinth
  will be hidden if it has not been setup. Otherwise, a warning is
  shown.

### Removed
- Removed init script and daemonize option.
- Removed writing to PID file.

### Security
- Fixed issue that could allow someone to start a module setup process
  without being logged in to Plinth.

[0.15.3]: https://github.com/freedombox/Plinth/compare/v0.15.2...v0.15.3
[0.15.2]: https://github.com/freedombox/Plinth/compare/v0.15.1...v0.15.2
[0.15.1]: https://github.com/freedombox/Plinth/compare/v0.15.0...v0.15.1
[0.15.0]: https://github.com/freedombox/Plinth/compare/v0.14.0...v0.15.0
[0.14.0]: https://github.com/freedombox/Plinth/compare/v0.13.1...v0.14.0
[0.13.1]: https://github.com/freedombox/Plinth/compare/v0.13.0...v0.13.1
[0.13.0]: https://github.com/freedombox/Plinth/compare/v0.12.0...v0.13.0
[0.12.0]: https://github.com/freedombox/Plinth/compare/v0.11.0...v0.12.0
[0.11.0]: https://github.com/freedombox/Plinth/compare/v0.10.0...v0.11.0
[0.10.0]: https://github.com/freedombox/Plinth/compare/v0.9.4...v0.10.0
[0.9.4]: https://github.com/freedombox/Plinth/compare/v0.9.3...v0.9.4
[0.9.3]: https://github.com/freedombox/Plinth/compare/v0.9.2...v0.9.3
