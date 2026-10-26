import logging
import azure.functions as func
from script import Weather
app = func.FunctionApp()
@app.timer_trigger(schedule="0 0 * * * *", arg_name="myTimer", run_on_startup=False,
              use_monitor=False) 
def WeatherLogger(myTimer: func.TimerRequest) -> None:
    if myTimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function executed.')
    
    script = Weather()
    extractingDataFromApi = script.extractingDataFromApi()
    cleaningUpData = script.cleaningUpData(extractingDataFromApi)
    
    logging.info(cleaningUpData)