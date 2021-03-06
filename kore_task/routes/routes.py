def includeme(config):
    config.add_static_view('static', '/static', cache_max_age=3600)
    config.add_route('login','/login')
    config.add_route('signout','/signout')
    config.add_route('password_token','/pass-token')
    config.add_route('change_password','/change-pass')
    config.add_route('capture_bill' , '/capture')
    config.add_route('view_bill','/bill/{hash:[0-9A-Z]{16}}')
    config.add_route('outflows', '/outflows')
    config.add_route('add_money', '/add-money')
    config.add_route('users', '/users')
    config.add_route('raise_reimbursement_ticket', '/raise-ticket')
    config.add_route('approve_ticket','/approve-ticket')