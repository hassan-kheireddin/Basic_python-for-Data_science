# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Hello.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: hkheired <hkheired@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/03/10 14:02:25 by hkheired          #+#    #+#              #
#    Updated: 2025/03/10 14:02:29 by hkheired         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

ft_list.remove("tata!")
ft_list += ["World!"]


# del ft_tuple
ft_tuple = ("Hello", "Lebanon!")


ft_set.remove("tutu!")
ft_set.add("Beirut!")

ft_dict["Hello"] = "42Beirut!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
