# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hkheired <hkheired@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 14:02:34 by hkheired          #+#    #+#              #
#    Updated: 2025/03/10 14:02:37 by hkheired         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import time

current_time = time.time()
current_date = time.localtime()

print(f"Seconds since January 1, 1970: {current_time:,.4f} \
or {current_time:.2e} in scientific notation")
print(time.strftime("%b %d %Y", current_date))
