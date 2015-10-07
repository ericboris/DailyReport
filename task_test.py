from task import Task

description = [
    # have keywords
        # has price
            # does not have addl. numbers
                'ext windows $288',             # ext 288
                'Gutters 288',                  # gutters 288
                'windows in-ext 288',           # in ext 288
                'windows in/out $288',          # in ext 288
            # have addl. numbers
                "roof-moss 288 need 28'",       # roof moss 288
                'facebook 25% off -%288',       # discount - 288
                'pw front $288 set up $288',    # pw front 288 \n setup 288
                'garage gutters 288 288'        # garage gutters 288
        # does not have price
            'windows in/out',
    # does not have keywords
        '',
        '288',
        "If 28' is too short",
        'already paid',
        '206-229-9288',
        '1,288 sqft',
        'townhomes are 288',
        '1:30pm parking lot 288'
]

description
    #has keyword
    job without price
    job with price and addl. numbers
    #does not have keywords
    telephone number
    only number
    blank line

job keywords
    windows
    gutters
    roof moss
    pw
    discount
    quote
    tax
    subtotal
    tip
    total
