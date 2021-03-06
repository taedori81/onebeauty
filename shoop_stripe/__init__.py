# -*- coding: utf-8 -*-
# This file is part of Shoop.
#
# Copyright (c) 2012-2015, Shoop Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.

from shoop.apps import AppConfig


class ShoopStripeAppConfig(AppConfig):
    name = "shoop_stripe"
    verbose_name = "Shoop Stripe Checkout integration"
    label = "shoop-stripe"
    provides = {
        "payment_method_module": [
            "shoop_stripe.module:StripeCheckoutModule",
        ]
    }


default_app_config = "shoop_stripe.ShoopStripeAppConfig"

