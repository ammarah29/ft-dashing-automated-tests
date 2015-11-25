Feature: Dashing Automation Tests

  Scenario Outline: Test the response time for dashing
    I make the request to dashing
    I should see response <status_code>
    Examples:
    | endpoint  | status_code |
    | Test      | 200         |

  Scenario Outline: Test the hardcoded endpoint
    I make a request to end point
    I should see a list of host names if tiles are black
    Examples:
    | endpoint  | status_code |
    | Test      | 200         |

  Scenario Outline: Grey tiles check
    I search for grey tiles

  Scenario Outline: Test the hardcoded endpoint
    I make a request to end point
    I should see a list of host names if tiles are black
    Examples:
    | endpoint  | status_code |
    | Test      | 200         |

  Scenario Outline: Grey tiles check
    I search for grey tiles
