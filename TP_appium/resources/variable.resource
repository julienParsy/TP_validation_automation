*** Variables ***
# Application
# Appium Server
${REMOTE_URL}        http://localhost:4723/wd/hub
${PLATFORM_NAME}     Android
${PLATFORM_VERSION}  15
${DEVICE_NAME}       emulator-5554

${R1}    ${EMPTY}
#    API Demos App
${API_DEMOS_APP_PACKAGE}        io.appium.android.apis
${API_DEMOS_APP_ACTIVITY}       io.appium.android.apis.ApiDemos

# Locator
${VIEWS}    //android.widget.TextView[@content-desc="Views"]
${ANIMATION_BUTTON}    //android.widget.TextView[@content-desc="Animation"]
${PUSH_BUTTON}    //android.widget.TextView[@content-desc="Push"]
${SELECT_ANIMATION}    //android.widget.TextView[@resource-id="android:id/text1"]
${HYPERSPACE}    //android.widget.CheckedTextView[@resource-id="android:id/text1" and @text="Hyperspace"]
${HYPERSPACE_MESSAGE}    //android.widget.TextView[@content-desc="a chance to be better."]
${CHRONOMETER}    //android.widget.TextView[@content-desc="Chronometer"]
${START_BUTTON}    //android.widget.Button[@content-desc="Start"]
${FORMAT_BUTTON}    io.appium.android.apis:id/set_format
${SEEKBAR_BUTTON}    //android.widget.TextView[@content-desc="Seek Bar"]
${SEEKBAR}    //android.widget.SeekBar[@resource-id="io.appium.android.apis:id/seek"]
${PROGRESS}    //android.widget.TextView[@resource-id="io.appium.android.apis:id/progress"]
