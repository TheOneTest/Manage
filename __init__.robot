*** Settings ***
Suite Setup       Setup_Pre_Conditaion
Library           OperatingSystem

*** Keywords ***
Setup_Testbed_variable
    #LAN PC INFO
    Set Environment Variable    G_HOST_NAME    ${EMPTY}    #记录主机IP地址
    #Set Environment Variable    G_HOST_IP    ${HOSTIP}
    #Path Info
    Set Environment Variable    G_SQAROOT    F:\\robotframework
    Set Environment Variable    G_LOG    %{G_SQAROOT}\\logs
    Set Environment Variable    G_CURRENTLOG    ${OUTPUT_DIR}

Setup_Website_variable
    LOG    空

Setup_Pre_Conditaion
    ${time}    Evaluate    datetime.datetime.now()    datetime
    Set Environment Variable    U_CUSTOM_TEST_TASK_START_TIME    ${time}
    Setup_Testbed_variable
    Setup_Website_variable
