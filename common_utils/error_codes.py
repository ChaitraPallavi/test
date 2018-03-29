class ErrorCodes:
    def __init__(self):
        pass

    ERROR_IN_REQUEST_DATA = 700
    ERROR_IN_CREATING_REWARDS_MEMBER = 701
    REWARD_MEMBER_ALREADY_EXISTS = 702
    REWARD_MEMBER_DOES_NOT_EXISTS = 711
    UNABLE_TO_ASSIGN_POINTS = 732
    SOURCE_REWARD_MEMBER_DOES_NOT_EXISTS = 741
    DESTINATION_REWARD_MEMBER_DOES_NOT_EXISTS = 742
    COUPON_NOT_AVAILABLE_REDEEM = 751
    INSUFFICIENT_POINTS = 752
    COUPON_DOES_NOT_EXISTS = 753
    POINTS_MIN_THRESHOLD_NOT_REACHED = 754
    COUPON_EXPIRED = 763
    COUPON_EVENT_NOT_STARTED = 764
    COUPON_EXCEEDED_MAX_USAGE = 765
    COUPON_NOT_ASSIGNED_TO_CUSTOMER = 766
    COUPON_CANNOT_BE_USED_CHANNEL = 767
    COUPON_NOT_USED = 771
    EVENT_CODE_NOT_FOUND = 781


error_codes_to_messages = {
    701: 'Unable to create rewards member',
    702: 'Rewards member already exists',
    711: 'Rewards member does not exists',
    732: 'Unable to assign points',
    741: 'Source rewards member does not exist',
    742: 'Destination rewards member does not exist',
    751: 'No coupon is available for redeemed amount',
    752: 'Insufficient points',
    753: 'Coupon does not exists',
    754: 'Points cannot be redeemed until you reach minimum threshold points',
    763: 'Coupon expired',
    764: 'Coupon event not started',
    765: 'Coupon exceeded maximum usage',
    766: 'Coupon is not assigned to this customer',
    767: 'Coupon cannot be used in this channel',
    771: 'Coupon has not been used',
    781: 'Event code not found',
}
