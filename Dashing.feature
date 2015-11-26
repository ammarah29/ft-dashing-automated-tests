Feature: Dashing Automation Tests

  Scenario Outline: Test the response status for dashing
    I make the request to dashing
    I should see response <status_code>
    Examples:
    | endpoint  | status_code |
    | Test      | 200         |

  Scenario Outline: Get all data ids and data urls
    I list all data ids with corresponding data urls

#
 # Scenario Outline: Black tiles check
  # I should see a list of host names if tiles are black


#  Scenario Outline: Grey tiles check
 #   I search for background dimgray
  #  If dimgray then check status code of data url

    #