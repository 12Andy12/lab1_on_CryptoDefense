import Fast_pow
import Evcklid
import Diffie_Hellman_protocol
import steps


Fast_pow.test(5, 20, 7)
Fast_pow.test1()


a = 28
b = 8

print("gcd({0}, {1}) = {2}".format(a, b, Evcklid.gcd(a, b)))

Oleg = Diffie_Hellman_protocol.CryptoUser()
Ivan = Diffie_Hellman_protocol.CryptoUser()
Oleg.generate_common_key(Ivan.get_my_public_key())
Ivan.generate_common_key(Oleg.get_my_public_key())

print("Oleg:\nPrivae_key = {0}\nPublic_key = {1}\nCommon_key = {2}".format(hex(Oleg.get_my_private_key()),
                                                                           hex(Oleg.get_my_public_key()),
                                                                           hex(Oleg.get_my_common_key())))

print("Ivan:\nPrivae_key = {0}\nPublic_key = {1}\nCommon_key = {2}".format(hex(Ivan.get_my_private_key()),
                                                                           hex(Ivan.get_my_public_key()),
                                                                           hex(Ivan.get_my_common_key())))

mes = Ivan.decrypt_message("Гиперцензурное выражение")

print("Ivan send mesage '{0}'".format(mes))
print("Oleg read mesage '{0}'".format(Oleg.encrypt_message(mes)))


steps.start()
