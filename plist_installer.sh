#Code from SuperUser user zekel: http://superuser.com/questions/943983/os-x-launchdaemon-not-running-service-could-not-initialize

// /Users/Hank/PycharmProjects/HW_scraper/Tests/shell_test.sh
#!/bin/sh -e
plist_path="/Users/Hank/PycharmProjects/HW_scraper/hw_scraper_launcher.plist"
plist_filename=$(hw_scraper_launcher1.plist "$plist_path")
install_path="/Users/Hank/Library/LaunchAgents/$plist_filename"

echo "installing launchctl plist: $plist_path --> $install_path"
sudo cp -f "$plist_path" "$install_path"
sudo chown root "$install_path"
sudo chmod 644 "$install_path"

sudo launchctl unload "$install_path"
sudo launchctl load "$install_path"

echo "to check if it's running, run this command: sudo launchctl list | grep wintr"
echo "to uninstall, run this command: sudo launchctl unload \"$install_path\""
