
import random
import time
import traceback

# 1. write this for an api call that can return 200 or any other error code
# 2. write this for an api call that returns an actual error

class CodeCommitApiError(Exception):
    def __init__(self):
        print(f'Error: AWS CodeCommit server is likely down, try again in a short amount of time')

class S3ApiError(Exception):
    def __init__(self):
        print(f'Error: AWS S3 server is likely down\n')

def retry(function_name, retry_count=3):
        def retry_wrapper(*args, **kwargs):
            counter = 0
            while counter <= retry_count:
                try:
                    return function_name(*args, **kwargs)

                except S3ApiError as error:
                    counter += 1
                    if counter <= retry_count:
                        print(f"Retrying {counter}/{retry_count}:")
                    else:
                        print(f"max amount of retries reached: {counter-1}/{retry_count}")
                        raise
                    time.sleep(.75)
                    
                except Exception as error:
                    print(traceback.format_exc())
                    counter += 1
                    if counter <= retry_count:
                        print(f"Retrying {counter}/{retry_count}:")
                    else:
                        print(f"max amount of retries reached: {counter-1}/{retry_count}")
                        raise CodeCommitApiError()
                    time.sleep(.75)
        return retry_wrapper


class Deployer():
    def __init__(self):
        self.STEP_COUNT = 0
        self.STEP_MAX = 2 

    def next_step_log_message(self):
            self.STEP_MAX = 2
            self.STEP_COUNT += 1
            print(f'\n')
            print(f'Step: {self.STEP_COUNT}/{self.STEP_MAX}')
            print(f'____________________________')
    
    @retry
    def codecommit_api_call(self, first_number, last_number):
        """case where api returns an actual error"""
        print(f'attempting to divide the given numbers: {first_number}/{last_number}')
        print(f'Answer to division: {first_number/last_number}')
    
    @retry
    def s3_api_call(self, first_number, last_number):
        """ case where api call can return 200 or anything else """
        # api_call_response = api.api_call(arg1, arg 2)
        response_code = random.randint(first_number, last_number)
        if response_code == 200:
            print(f'Success: {response_code}')
            return response_code
        else:
            print(f'Fail: {response_code}')
            raise S3ApiError()
    

# now this is the "high level function", which is sitting in another file
# ________________________________________________________________
@retry
def high_level_function():
    print('high level function begining')
    deployer = Deployer()
    try:
        deployer.next_step_log_message()
        deployer.codecommit_api_call(5,1)
        
        deployer.next_step_log_message()
        deployer.s3_api_call(400,550)
        
        print('\n___________________________________________')
        print('high level function completed successfully')
    except CodeCommitApiError:
        print('\nHigh level function did not complete')
        print('Retrying entire app flow')
        raise
    except S3ApiError:
        print('AWS S3 server appears to be down')
        print(f"Try again in a short amount of time")
        print('\nHigh level function did not complete')
        print('Retrying entire app flow')
        raise
    except Exception:
        print(traceback.format_exc())
        print('\nHigh level function did not complete')
        print('Retrying entire app flow')
    finally:
        print('Cleaning up temporary files\n\n\n')

print('executing high level function')
high_level_function()
