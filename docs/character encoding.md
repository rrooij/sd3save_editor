# Character Encoding

When converting from unicode to cartridge, more than one unicode codepoint can be mapped to one cartridge codepoint. On the other hand, when converting from cartridge to unicode, only one unicode codepoint will be assigned. For example, the ASCII A and the fullwidth A will both be mapped to the cartridge A. In reverse, the cartridge A will only be mapped to the ASCII A and not the fullwidth A.

**Remarks**

Characters in the ASCII range

- The different language encodings basically follow the ASCII encoding, followed by a number of additional characters in the range from 007F to 009F. The only exception is the Spanish encoding where the lower case characters happen to be shifted.
- When converting from cartridge to unicode, the character in the ASCII range is chosen over any other variants.
- The only exception is the Japanese fullwidth encoding, which chooses the fullwidth character over the others.
- There is also a small number of characters in the ASCII range where the visual glyph used in the cartridge encoding actually resembles a unicode character outside of the ASCII range. In particular, these characters are the asterisk operator, the minus sign, the broken bar, and the small tilde. Yet, when converting back, the codepoint from the ASCII range is to be used.

Hiragana, Katakana and Kanji

- All hiragana and katakana are being encoded, however, kanji are not supported. This includes the three kanji for time/month/day in the ASCII range as well.

Other Characters

- Regarding the middle dot, there are a variety of possible unicode codepoints. However, we are going for the katakana middle dot when converting back.
- Regarding the heart, both the black heart suit and the heavy black heart are viable unicode codepoints. However, we are going for the black heart suit when converting back.
- There are many codepoints for arrows in Unicode. The ones that fit the most visually are the heavy arrows. However, we are going for the standard arrows when converting back.

**Regarding the order of codepoints within the JSON files**

European Languages

1. ASCII characters
2. ASCII characters (fullwidth)
3. ASCII character variants
4. Language specific characters

Japanese

1. ASCII characters
2. ASCII characters (fullwidth)
3. ASCII character variants
4. Japanese specific characters (ASCII range)
5. Japanese specific characters (other range)
6. Hiragana and katakana characters

### Basic ASCII

| Cartridge | Unicode |
| --- | --- |
| 0020 [ ] | U+0020 SPACE (SP) [ ]<br/>U+3000 IDEOGRAPHIC SPACE [　] |
| 0021 [!] | U+0021 EXCLAMATION MARK [!]<br/>U+FF01 FULLWIDTH EXCLAMATION MARK [！] |
| 0022 ["] | U+0022 QUOTATION MARK ["]<br/>U+FF02 FULLWIDTH QUOTATION MARK [＂] |
| 0023 [#] | U+0023 NUMBER SIGN [#]<br/>U+FF03 FULLWIDTH NUMBER SIGN [＃] |
| 0024 [$] | U+0024 DOLLAR SIGN [$]<br/>U+FF04 FULLWIDTH DOLLAR SIGN [＄] |
| 0025 [%] | U+0025 PERCENT SIGN [%]<br/>U+FF05 FULLWIDTH PERCENT SIGN [％] |
| 0026 [&] | U+0026 AMPERSAND [&]<br/>U+FF06 FULLWIDTH AMPERSAND [＆] |
| 0027 ['] | U+0027 APOSTROPHE [']<br/>U+FF07 FULLWIDTH APOSTROPHE [＇] |
| 0028 [(] | U+0028 LEFT PARENTHESIS [(]<br/>U+FF08 FULLWIDTH LEFT PARENTHESIS [（] |
| 0029 [)] | U+0029 RIGHT PARENTHESIS [)]<br/>U+FF09 FULLWIDTH RIGHT PARENTHESIS [）] |
| 002A [∗] | U+002A ASTERISK [*]<br/>U+2217 ASTERISK OPERATOR [∗]<br/>U+FF0A FULLWIDTH ASTERISK [＊] |
| 002B [+] | U+002B PLUS SIGN [+]<br/>U+FF0B FULLWIDTH PLUS SIGN [＋] |
| 002C [,] | U+002C COMMA [,]<br/>U+FF0C FULLWIDTH COMMA [，] |
| 002D [−] | U+002D HYPHEN-MINUS [-]<br/>U+2212 MINUS SIGN [−]<br/>U+FF0D FULLWIDTH HYPHEN-MINUS [－] ||
| 002E [.] | U+0030 FULL STOP [.]<br/>U+FF0E FULLWIDTH FULL STOP [．] |
| 002F [/] | U+0030 SOLIDUS [/]<br/>U+FF0F FULLWIDTH SOLIDUS [／] |
| 0030 [0] | U+0030 DIGIT ZERO [0]<br/>U+FF10 FULLWIDTH DIGIT ZERO [０] |
| 0031 [1] | U+0030 DIGIT ZERO [1]<br/>U+FF11 FULLWIDTH DIGIT ZERO [１] |
| 0032 [2] | U+0030 DIGIT ZERO [2]<br/>U+FF12 FULLWIDTH DIGIT ZERO [２] |
| 0033 [3] | U+0030 DIGIT ZERO [3]<br/>U+FF13 FULLWIDTH DIGIT ZERO [３] |
| 0034 [4] | U+0030 DIGIT ZERO [4]<br/>U+FF14 FULLWIDTH DIGIT ZERO [４] |
| 0035 [5] | U+0030 DIGIT ZERO [5]<br/>U+FF15 FULLWIDTH DIGIT ZERO [５] |
| 0036 [6] | U+0030 DIGIT ZERO [6]<br/>U+FF16 FULLWIDTH DIGIT ZERO [６] |
| 0037 [7] | U+0030 DIGIT ZERO [7]<br/>U+FF17 FULLWIDTH DIGIT ZERO [７] |
| 0038 [8] | U+0030 DIGIT ZERO [8]<br/>U+FF18 FULLWIDTH DIGIT ZERO [８] |
| 0039 [9] | U+0030 DIGIT ZERO [9]<br/>U+FF19 FULLWIDTH DIGIT ZERO [９] |
| 003A [:] | U+003A COLON [:]<br/>U+FF1A FULLWIDTH COLON [：] |
| 003B [;] | U+003B SEMICOLON [;]<br/>U+FF1B FULLWIDTH SEMICOLON [；] |
| 003C [<] | U+003C LESS-THAN SIGN [<]<br/>U+FF1C FULLWIDTH LESS-THAN SIGN [＜] |
| 003D [=] | U+003D EQUALS SIGN [=]<br/>U+FF1D FULLWIDTH EQUALS SIGN [＝] |
| 003E [>] | U+003E GREATER-THAN SIGN [>]<br/>U+FF1E FULLWIDTH GREATER-THAN SIGN [＞] |
| 003F [?] | U+003F QUESTION MARK [?]<br/>U+FF1F FULLWIDTH QUESTION MARK [？] |
| 0040 [@] | U+0040 COMMERCIAL AT [@]<br/>U+FF20 FULLWIDTH COMMERCIAL AT [＠] |
| 0041 [A] | U+0061 LATIN CAPITAL LETTER A [A]<br/>U+FF41 FULLWIDTH LATIN CAPITAL LETTER A [Ａ] |
| 0042 [B] | U+0062 LATIN CAPITAL LETTER B [B]<br/>U+FF42 FULLWIDTH LATIN CAPITAL LETTER B [Ｂ] |
| 0043 [C] | U+0063 LATIN CAPITAL LETTER C [C]<br/>U+FF43 FULLWIDTH LATIN CAPITAL LETTER C [Ｃ] |
| 0044 [D] | U+0064 LATIN CAPITAL LETTER D [D]<br/>U+FF44 FULLWIDTH LATIN CAPITAL LETTER D [Ｄ] |
| 0045 [E] | U+0065 LATIN CAPITAL LETTER E [E]<br/>U+FF45 FULLWIDTH LATIN CAPITAL LETTER E [Ｅ] |
| 0046 [F] | U+0066 LATIN CAPITAL LETTER F [F]<br/>U+FF46 FULLWIDTH LATIN CAPITAL LETTER F [Ｆ] |
| 0047 [G] | U+0067 LATIN CAPITAL LETTER G [G]<br/>U+FF47 FULLWIDTH LATIN CAPITAL LETTER G [Ｇ] |
| 0048 [H] | U+0068 LATIN CAPITAL LETTER H [H]<br/>U+FF48 FULLWIDTH LATIN CAPITAL LETTER H [Ｈ] |
| 0049 [I] | U+0069 LATIN CAPITAL LETTER I [I]<br/>U+FF49 FULLWIDTH LATIN CAPITAL LETTER I [Ｉ] |
| 004A [J] | U+006A LATIN CAPITAL LETTER J [J]<br/>U+FF4A FULLWIDTH LATIN CAPITAL LETTER J [Ｊ] |
| 004B [K] | U+006B LATIN CAPITAL LETTER K [K]<br/>U+FF4B FULLWIDTH LATIN CAPITAL LETTER K [Ｋ] |
| 004C [L] | U+006C LATIN CAPITAL LETTER L [L]<br/>U+FF4C FULLWIDTH LATIN CAPITAL LETTER L [Ｌ] |
| 004D [M] | U+006D LATIN CAPITAL LETTER M [M]<br/>U+FF4D FULLWIDTH LATIN CAPITAL LETTER M [Ｍ] |
| 004E [N] | U+006E LATIN CAPITAL LETTER N [N]<br/>U+FF4E FULLWIDTH LATIN CAPITAL LETTER N [Ｎ] |
| 004F [O] | U+006F LATIN CAPITAL LETTER O [O]<br/>U+FF4F FULLWIDTH LATIN CAPITAL LETTER O [Ｏ] |
| 0050 [P] | U+0070 LATIN CAPITAL LETTER P [P]<br/>U+FF50 FULLWIDTH LATIN CAPITAL LETTER P [Ｐ] |
| 0051 [Q] | U+0071 LATIN CAPITAL LETTER Q [Q]<br/>U+FF51 FULLWIDTH LATIN CAPITAL LETTER Q [Ｑ] |
| 0052 [R] | U+0072 LATIN CAPITAL LETTER R [R]<br/>U+FF52 FULLWIDTH LATIN CAPITAL LETTER R [Ｒ] |
| 0053 [S] | U+0073 LATIN CAPITAL LETTER S [S]<br/>U+FF53 FULLWIDTH LATIN CAPITAL LETTER S [Ｓ] |
| 0054 [T] | U+0074 LATIN CAPITAL LETTER T [T]<br/>U+FF54 FULLWIDTH LATIN CAPITAL LETTER T [Ｔ] |
| 0055 [U] | U+0075 LATIN CAPITAL LETTER U [U]<br/>U+FF55 FULLWIDTH LATIN CAPITAL LETTER U [Ｕ] |
| 0056 [V] | U+0076 LATIN CAPITAL LETTER V [V]<br/>U+FF56 FULLWIDTH LATIN CAPITAL LETTER V [Ｖ] |
| 0057 [W] | U+0077 LATIN CAPITAL LETTER W [W]<br/>U+FF57 FULLWIDTH LATIN CAPITAL LETTER W [Ｗ] |
| 0058 [X] | U+0078 LATIN CAPITAL LETTER X [X]<br/>U+FF58 FULLWIDTH LATIN CAPITAL LETTER X [Ｘ] |
| 0059 [Y] | U+0079 LATIN CAPITAL LETTER Y [Y]<br/>U+FF59 FULLWIDTH LATIN CAPITAL LETTER Y [Ｙ] |
| 005A [Z] | U+007A LATIN CAPITAL LETTER Z [Z]<br/>U+FF5A FULLWIDTH LATIN CAPITAL LETTER Z [Ｚ] |
| 005B [[] | U+005B LEFT SQUARE BRACKET [[]<br/>U+FF3B FULLWIDTH LEFT SQUARE BRACKET [［] |
| 005C [\\] | U+005C REVERSE SOLIDUS [\\]<br/>U+FF3C FULLWIDTH REVERSE SOLIDUS [＼] |
| 005D []] | U+005D RIGHT SQUARE BRACKET []]<br/>U+FF3D FULLWIDTH RIGHT SQUARE BRACKET [］] |
| 005E [^] | U+005E CIRCUMFLEX ACCENT [^]<br/>U+FF3E FULLWIDTH CIRCUMFLEX ACCENT [＾] |
| 005F [_] | U+005F LOW LINE [_]<br/>U+FF3F FULLWIDTH LOW LINE [＿] |
| 0060 [\`] | U+0060 GRAVE ACCENT [\`]<br/>U+FF40 FULLWIDTH GRAVE ACCENT [｀] |
| 0061 [a] | U+0061 LATIN SMALL LETTER A [a]<br/>U+FF41 FULLWIDTH LATIN SMALL LETTER A [ａ] |
| 0062 [b] | U+0062 LATIN SMALL LETTER B [b]<br/>U+FF42 FULLWIDTH LATIN SMALL LETTER B [ｂ] |
| 0063 [c] | U+0063 LATIN SMALL LETTER C [c]<br/>U+FF43 FULLWIDTH LATIN SMALL LETTER C [ｃ] |
| 0064 [d] | U+0064 LATIN SMALL LETTER D [d]<br/>U+FF44 FULLWIDTH LATIN SMALL LETTER D [ｄ] |
| 0065 [e] | U+0065 LATIN SMALL LETTER E [e]<br/>U+FF45 FULLWIDTH LATIN SMALL LETTER E [ｅ] |
| 0066 [f] | U+0066 LATIN SMALL LETTER F [f]<br/>U+FF46 FULLWIDTH LATIN SMALL LETTER F [ｆ] |
| 0067 [g] | U+0067 LATIN SMALL LETTER G [g]<br/>U+FF47 FULLWIDTH LATIN SMALL LETTER G [ｇ] |
| 0068 [h] | U+0068 LATIN SMALL LETTER H [h]<br/>U+FF48 FULLWIDTH LATIN SMALL LETTER H [ｈ] |
| 0069 [i] | U+0069 LATIN SMALL LETTER I [i]<br/>U+FF49 FULLWIDTH LATIN SMALL LETTER I [ｉ] |
| 006A [j] | U+006A LATIN SMALL LETTER J [j]<br/>U+FF4A FULLWIDTH LATIN SMALL LETTER J [ｊ] |
| 006B [k] | U+006B LATIN SMALL LETTER K [k]<br/>U+FF4B FULLWIDTH LATIN SMALL LETTER K [ｋ] |
| 006C [l] | U+006C LATIN SMALL LETTER L [l]<br/>U+FF4C FULLWIDTH LATIN SMALL LETTER L [ｌ] |
| 006D [m] | U+006D LATIN SMALL LETTER M [m]<br/>U+FF4D FULLWIDTH LATIN SMALL LETTER M [ｍ] |
| 006E [n] | U+006E LATIN SMALL LETTER N [n]<br/>U+FF4E FULLWIDTH LATIN SMALL LETTER N [ｎ] |
| 006F [o] | U+006F LATIN SMALL LETTER O [o]<br/>U+FF4F FULLWIDTH LATIN SMALL LETTER O [ｏ] |
| 0070 [p] | U+0070 LATIN SMALL LETTER P [p]<br/>U+FF50 FULLWIDTH LATIN SMALL LETTER P [ｐ] |
| 0071 [q] | U+0071 LATIN SMALL LETTER Q [q]<br/>U+FF51 FULLWIDTH LATIN SMALL LETTER Q [ｑ] |
| 0072 [r] | U+0072 LATIN SMALL LETTER R [r]<br/>U+FF52 FULLWIDTH LATIN SMALL LETTER R [ｒ] |
| 0073 [s] | U+0073 LATIN SMALL LETTER S [s]<br/>U+FF53 FULLWIDTH LATIN SMALL LETTER S [ｓ] |
| 0074 [t] | U+0074 LATIN SMALL LETTER T [t]<br/>U+FF54 FULLWIDTH LATIN SMALL LETTER T [ｔ] |
| 0075 [u] | U+0075 LATIN SMALL LETTER U [u]<br/>U+FF55 FULLWIDTH LATIN SMALL LETTER U [ｕ] |
| 0076 [v] | U+0076 LATIN SMALL LETTER V [v]<br/>U+FF56 FULLWIDTH LATIN SMALL LETTER V [ｖ] |
| 0077 [w] | U+0077 LATIN SMALL LETTER W [w]<br/>U+FF57 FULLWIDTH LATIN SMALL LETTER W [ｗ] |
| 0078 [x] | U+0078 LATIN SMALL LETTER X [x]<br/>U+FF58 FULLWIDTH LATIN SMALL LETTER X [ｘ] |
| 0079 [y] | U+0079 LATIN SMALL LETTER Y [y]<br/>U+FF59 FULLWIDTH LATIN SMALL LETTER Y [ｙ] |
| 007A [z] | U+007A LATIN SMALL LETTER Z [z]<br/>U+FF5A FULLWIDTH LATIN SMALL LETTER Z [ｚ] |
| 007B [{] | U+007B LEFT CURLY BRACKET [{]<br/>U+FF5B FULLWIDTH LEFT CURLY BRACKET [｛] |
| 007C [¦] | U+007C VERTICAL LINE [\|]<br/>U+00A6 BROKEN BAR [¦]<br/>U+FF5C FULLWIDTH VERTICAL LINE [｜]<br/>U+FFE4 FULLWIDTH BROKEN BAR [￤] |
| 007D [}] | U+007D RIGHT CURLY BRACKET [}]<br/>U+FF5D FULLWIDTH RIGHT CURLY BRACKET [｝] |
| 007E [˜] | U+007E TILDE [~]<br/>U+02DC SMALL TILDE [˜]<br/>U+FF5E FULLWIDTH TILDE [～] |

### Japanese Kana

| Cartridge | Unicode |
| --- | --- |
| 007F [あ] | U+3042 HIRAGANA LETTER A [あ] |
| 0080 [い] | U+3044 HIRAGANA LETTER I [い] |
| 0081 [う] | U+3046 HIRAGANA LETTER U [う] |
| 0082 [え] | U+3048 HIRAGANA LETTER E [え] |
| 0083 [お] | U+304A HIRAGANA LETTER O [お] |
| 0084 [か] | U+304B HIRAGANA LETTER KA [か] |
| 0085 [き] | U+304D HIRAGANA LETTER KI [き] |
| 0086 [く] | U+304F HIRAGANA LETTER KU [く] |
| 0087 [け] | U+3051 HIRAGANA LETTER KE [け] |
| 0088 [こ] | U+3053 HIRAGANA LETTER KO [こ] |
| 0089 [さ] | U+3055 HIRAGANA LETTER SA [さ] |
| 008A [し] | U+3057 HIRAGANA LETTER SI [し] |
| 008B [す] | U+3059 HIRAGANA LETTER SU [す] |
| 008C [せ] | U+305B HIRAGANA LETTER SE [せ] |
| 008D [そ] | U+305D HIRAGANA LETTER SO [そ] |
| 008E [た] | U+305F HIRAGANA LETTER TA [た] |
| 008F [ち] | U+3061 HIRAGANA LETTER TI [ち] |
| 0090 [つ] | U+3064 HIRAGANA LETTER TU [つ] |
| 0091 [て] | U+3066 HIRAGANA LETTER TE [て] |
| 0092 [と] | U+3068 HIRAGANA LETTER TO [と] |
| 0093 [な] | U+306A HIRAGANA LETTER NA [な] |
| 0094 [に] | U+306B HIRAGANA LETTER NI [に] |
| 0095 [ぬ] | U+306C HIRAGANA LETTER NU [ぬ] |
| 0096 [ね] | U+306D HIRAGANA LETTER NE [ね] |
| 0097 [の] | U+306E HIRAGANA LETTER NO [の] |
| 0098 [は] | U+306F HIRAGANA LETTER HA [は] |
| 0099 [ひ] | U+3072 HIRAGANA LETTER HI [ひ] |
| 009A [ふ] | U+3075 HIRAGANA LETTER HU [ふ] |
| 009B [へ] | U+3078 HIRAGANA LETTER HE [へ] |
| 009C [ほ] | U+307B HIRAGANA LETTER HO [ほ] |
| 009D [ま] | U+307E HIRAGANA LETTER MA [ま] |
| 009E [み] | U+307F HIRAGANA LETTER MI [み] |
| 009F [む] | U+3080 HIRAGANA LETTER MU [む] |
| 00A0 [め] | U+3081 HIRAGANA LETTER ME [め] |
| 00A1 [も] | U+3082 HIRAGANA LETTER MO [も] |
| 00A2 [や] | U+3084 HIRAGANA LETTER YA [や] |
| 00A3 [ゆ] | U+3086 HIRAGANA LETTER YU [ゆ] |
| 00A4 [よ] | U+3088 HIRAGANA LETTER YO [よ] |
| 00A5 [ら] | U+3089 HIRAGANA LETTER RA [ら] |
| 00A6 [り] | U+308A HIRAGANA LETTER RI [り] |
| 00A7 [る] | U+308B HIRAGANA LETTER RU [る] |
| 00A8 [れ] | U+308C HIRAGANA LETTER RE [れ] |
| 00A9 [ろ] | U+308D HIRAGANA LETTER RO [ろ] |
| 00AA [わ] | U+308F HIRAGANA LETTER WA [わ] |
| 00AB [を] | U+3092 HIRAGANA LETTER WO [を] |
| 00AC [ん] | U+3093 HIRAGANA LETTER N [ん] |
| 00AD [っ] | U+3063 HIRAGANA LETTER SMALL TU [っ] |
| 00AE [ゃ] | U+3083 HIRAGANA LETTER SMALL YA [ゃ] |
| 00AF [ゅ] | U+3085 HIRAGANA LETTER SMALL YU [ゅ] |
| 00B0 [ょ] | U+3087 HIRAGANA LETTER SMALL YO [ょ] |
| 00B1 [ぁ] | U+3041 HIRAGANA LETTER SMALL A [ぁ] |
| 00B2 [ぃ] | U+3043 HIRAGANA LETTER SMALL I [ぃ] |
| 00B3 [ぅ] | U+3045 HIRAGANA LETTER SMALL U [ぅ] |
| 00B4 [ぇ] | U+3047 HIRAGANA LETTER SMALL E [ぇ] |
| 00B5 [ぉ] | U+3049 HIRAGANA LETTER SMALL O [ぉ] |
| 00B6 [ッ] | U+30C3 KATAKANA LETTER SMALL TU [ッ] |
| 00B7 [ャ] | U+30E3 KATAKANA LETTER SMALL YA [ャ] |
| 00B8 [ュ] | U+30E5 KATAKANA LETTER SMALL YU [ュ] |
| 00B9 [ョ] | U+30E7 KATAKANA LETTER SMALL YO [ョ] |
| 00BA [ァ] | U+30A1 KATAKANA LETTER SMALL A [ァ] |
| 00BB [ィ] | U+30A3 KATAKANA LETTER SMALL I [ィ] |
| 00BC [ゥ] | U+30A5 KATAKANA LETTER SMALL U [ゥ] |
| 00BD [ェ] | U+30A7 KATAKANA LETTER SMALL E [ェ] |
| 00BE [ォ] | U+30A9 KATAKANA LETTER SMALL O [ォ] |
| 00BF [ア] | U+30A2 KATAKANA LETTER A [ア] |
| 00C0 [イ] | U+30A4 KATAKANA LETTER I [イ] |
| 00C1 [ウ] | U+30A6 KATAKANA LETTER U [ウ] |
| 00C2 [エ] | U+30A8 KATAKANA LETTER E [エ] |
| 00C3 [オ] | U+30AA KATAKANA LETTER O [オ] |
| 00C4 [カ] | U+30AB KATAKANA LETTER KA [カ] |
| 00C5 [キ] | U+30AD KATAKANA LETTER KI [キ] |
| 00C6 [ク] | U+30AF KATAKANA LETTER KU [ク] |
| 00C7 [ケ] | U+30B1 KATAKANA LETTER KE [ケ] |
| 00C8 [コ] | U+30B3 KATAKANA LETTER KO [コ] |
| 00C9 [サ] | U+30B5 KATAKANA LETTER SA [サ] |
| 00CA [シ] | U+30B7 KATAKANA LETTER SI [シ] |
| 00CB [ス] | U+30B9 KATAKANA LETTER SU [ス] |
| 00CC [セ] | U+30BB KATAKANA LETTER SE [セ] |
| 00CD [ソ] | U+30BD KATAKANA LETTER SO [ソ] |
| 00CE [タ] | U+30BF KATAKANA LETTER TA [タ] |
| 00CF [チ] | U+30C1 KATAKANA LETTER TI [チ] |
| 00D0 [ツ] | U+30C4 KATAKANA LETTER TU [ツ] |
| 00D1 [テ] | U+30C6 KATAKANA LETTER TE [テ] |
| 00D2 [ト] | U+30C8 KATAKANA LETTER TO [ト] |
| 00D3 [ナ] | U+30CA KATAKANA LETTER NA [ナ] |
| 00D4 [ニ] | U+30CB KATAKANA LETTER NI [ニ] |
| 00D5 [ヌ] | U+30CC KATAKANA LETTER NU [ヌ] |
| 00D6 [ネ] | U+30CD KATAKANA LETTER NE [ネ] |
| 00D7 [ノ] | U+30CE KATAKANA LETTER NO [ノ] |
| 00D8 [ハ] | U+30CF KATAKANA LETTER HA [ハ] |
| 00D9 [ヒ] | U+30D2 KATAKANA LETTER HI [ヒ] |
| 00DA [フ] | U+30D5 KATAKANA LETTER HU [フ] |
| 00DB [ヘ] | U+30D8 KATAKANA LETTER HE [ヘ] |
| 00DC [ホ] | U+30DB KATAKANA LETTER HO [ホ] |
| 00DD [マ] | U+30DE KATAKANA LETTER MA [マ] |
| 00DE [ミ] | U+30DF KATAKANA LETTER MI [ミ] |
| 00DF [ム] | U+30E0 KATAKANA LETTER MU [ム] |
| 00E0 [メ] | U+30E1 KATAKANA LETTER ME [メ] |
| 00E1 [モ] | U+30E2 KATAKANA LETTER MO [モ] |
| 00E2 [ヤ] | U+30E4 KATAKANA LETTER YA [ヤ] |
| 00E3 [ユ] | U+30E6 KATAKANA LETTER YU [ユ] |
| 00E4 [ヨ] | U+30E8 KATAKANA LETTER YO [ヨ] |
| 00E5 [ラ] | U+30E9 KATAKANA LETTER RA [ラ] |
| 00E6 [リ] | U+30EA KATAKANA LETTER RI [リ] |
| 00E7 [ル] | U+30EB KATAKANA LETTER RU [ル] |
| 00E8 [レ] | U+30EC KATAKANA LETTER RE [レ] |
| 00E9 [ロ] | U+30ED KATAKANA LETTER RO [ロ] |
| 00EA [ワ] | U+30EF KATAKANA LETTER WA [ワ] |
| 00EB [ヲ] | U+30F2 KATAKANA LETTER WO [ヲ] |
| 00EC [ン] | U+30F3 KATAKANA LETTER N [ン] |
| 00ED [が] | U+304C HIRAGANA LETTER GA [が] |
| 00EE [ぎ] | U+304E HIRAGANA LETTER GI [ぎ] |
| 00EF [ぐ] | U+3050 HIRAGANA LETTER GU [ぐ] |
| 00F0 [げ] | U+3052 HIRAGANA LETTER GE [げ] |
| 00F1 [ご] | U+3054 HIRAGANA LETTER GO [ご] |
| 00F2 [ざ] | U+3056 HIRAGANA LETTER ZA [ざ] |
| 00F3 [じ] | U+3058 HIRAGANA LETTER ZI [じ] |
| 00F4 [ず] | U+305A HIRAGANA LETTER ZU [ず] |
| 00F5 [ぜ] | U+305C HIRAGANA LETTER ZE [ぜ] |
| 00F6 [ぞ] | U+305E HIRAGANA LETTER ZO [ぞ] |
| 00F7 [だ] | U+3060 HIRAGANA LETTER DA [だ] |
| 00F8 [ぢ] | U+3062 HIRAGANA LETTER DI [ぢ] |
| 00F9 [づ] | U+3065 HIRAGANA LETTER DU [づ] |
| 00FA [で] | U+3067 HIRAGANA LETTER DE [で] |
| 00FB [ど] | U+3069 HIRAGANA LETTER DO [ど] |
| 00FC [ば] | U+3070 HIRAGANA LETTER BA [ば] |
| 00FD [び] | U+3073 HIRAGANA LETTER BI [び] |
| 00FE [ぶ] | U+3076 HIRAGANA LETTER BU [ぶ] |
| 00FF [べ] | U+3079 HIRAGANA LETTER BE [べ] |
| 0100 [ぼ] | U+307C HIRAGANA LETTER BO [ぼ] |
| 0101 [ガ] | U+30AC KATAKANA LETTER GA [ガ] |
| 0102 [ギ] | U+30AE KATAKANA LETTER GI [ギ] |
| 0103 [グ] | U+30B0 KATAKANA LETTER GU [グ] |
| 0104 [ゲ] | U+30B2 KATAKANA LETTER GE [ゲ] |
| 0105 [ゴ] | U+30B4 KATAKANA LETTER GO [ゴ] |
| 0106 [ザ] | U+30B6 KATAKANA LETTER ZA [ザ] |
| 0107 [ジ] | U+30B8 KATAKANA LETTER ZI [ジ] |
| 0108 [ズ] | U+30BA KATAKANA LETTER ZU [ズ] |
| 0109 [ゼ] | U+30BC KATAKANA LETTER ZE [ゼ] |
| 010A [ゾ] | U+30BE KATAKANA LETTER ZO [ゾ] |
| 010B [ダ] | U+30C0 KATAKANA LETTER DA [ダ] |
| 010C [ヂ] | U+30C2 KATAKANA LETTER DI [ヂ] |
| 010D [ヅ] | U+30C5 KATAKANA LETTER DU [ヅ] |
| 010E [デ] | U+30C7 KATAKANA LETTER DE [デ] |
| 010F [ド] | U+30C9 KATAKANA LETTER DO [ド] |
| 0110 [バ] | U+30D0 KATAKANA LETTER BA [バ] |
| 0111 [ビ] | U+30D3 KATAKANA LETTER BI [ビ] |
| 0112 [ブ] | U+30D6 KATAKANA LETTER BU [ブ] |
| 0113 [ベ] | U+30D9 KATAKANA LETTER BE [ベ] |
| 0114 [ボ] | U+30DC KATAKANA LETTER BO [ボ] |
| 0115 [ヴ] | U+30F4 KATAKANA LETTER VU [ヴ] |
| 0116 [ぱ] | U+3071 HIRAGANA LETTER PA [ぱ] |
| 0117 [ぴ] | U+3074 HIRAGANA LETTER PI [ぴ] |
| 0118 [ぷ] | U+3077 HIRAGANA LETTER PU [ぷ] |
| 0119 [ぺ] | U+307A HIRAGANA LETTER PE [ぺ] |
| 011A [ぽ] | U+307D KATAKANA LETTER PO [ぽ] |
| 011B [パ] | U+30D1 KATAKANA LETTER PA [パ] |
| 011C [ピ] | U+30D4 KATAKANA LETTER PI [ピ] |
| 011D [プ] | U+30D7 KATAKANA LETTER PU [プ] |
| 011E [ペ] | U+30DA KATAKANA LETTER PE [ペ] |
| 011F [ポ] | U+30DD KATAKANA LETTER PO [ポ] |

### Japanese Additions

| Cartridge | Unicode |
| --- | --- |
| 0022 [”] | U+201D RIGHT DOUBLE QUOTATION MARK [”] |
| 0023 [“] | U+201C LEFT DOUBLE QUOTATION MARK [“] |
| 0024 [▼] | U+25BC BLACK DOWN-POINTING TRIANGLE [▼] |
| 0026 [‘] | U+2018 LEFT SINGLE QUOTATION MARK [‘] |
| 0027 [’] | U+2019 RIGHT SINGLE QUOTATION MARK [’] |
| 003B [「] | U+300C LEFT CORNER BRACKET [「]<br/>U+FF62 HALFWIDTH LEFT CORNER BRACKET [｢] |
| 003C [」] | U+300D RIGHT CORNER BRACKET [」]<br/>U+FF63 HALFWIDTH RIGHT CORNER BRACKET [｣] |
| 003E [○] | U+25CB WHITE CIRCLE [○] |
| 0040 [●] | U+25CF BLACK CIRCLE [●] |
| 005B [×] | U+00D7 MULTIPLICATION SIGN [×] |
| 005C […] | U+2026 HORIZONTAL ELLIPSIS […] |
| 005D | N/A (1) |
| 005E | N/A (1) |
| 005F | N/A (1) |
| 0060 [〜] | U+007E TILDE [~]<br/>U+02DC SMALL TILDE [˜]<br/>U+FF5E FULLWIDTH TILDE [～] |
| 007B [、] | U+3001 IDEOGRAPHIC COMMA [、]<br/>U+FF64 HALFWIDTH IDEOGRAPHIC COMMA [､] |
| 007C [。] | U+3002 IDEOGRAPHIC FULL STOP [。]<br/>U+FF61 HALFWIDTH IDEOGRAPHIC FULL STOP [｡] |
| 007D [ー] | U+30FC KATAKANA-HIRAGANA PROLONGED SOUND MARK [ー]<br/>U+FF70 HALFWIDTH KATAKANA-HIRAGANA PROLONGED SOUND MARK [ｰ] |
| 007E [♥] | U+2665 BLACK HEART SUIT [♥]<br/>U+2764 HEAVY BLACK HEART [❤] |
| 0120 [『] | U+300E LEFT WHITE CORNER BRACKET [『] |
| 012B [＿] | U+005F LOW LINE [_]<br/>U+FF3F FULLWIDTH LOW LINE [＿] |
| 0163 [』] | U+300F RIGHT WHITE CORNER BRACKET [』] |
| 01AF [・] | U+00B7 MIDDLE DOT [·]<br/>U+2022 BULLET [•]<br/>U+30FB KATAKANA MIDDLE DOT [・]<br/>U+FF65 HALFWIDTH KATAKANA MIDDLE DOT [･] |
| 020F [🡆] | U+2192 RIGHTWARDS ARROW [→]<br/>U+2B95 RIGHTWARDS BLACK ARROW [⮕]<br/>U+FFEB HALFWIDTH RIGHTWARDS ARROW [￫]<br/>U+1F846 RIGHTWARDS HEAVY ARROW [🡆] |
| 0245 [【] | U+3010 LEFT BLACK LENTICULAR BRACKET [【] |
| 0246 [】] | U+3011 RIGHT BLACK LENTICULAR BRACKET [】] |
| 0290 [［] | U+005B LEFT SQUARE BRACKET [[]<br/>U+FF3B FULLWIDTH LEFT SQUARE BRACKET [［] |
| 0291 [］] | U+005D RIGHT SQUARE BRACKET []]<br/>U+FF3D FULLWIDTH RIGHT SQUARE BRACKET [］] |
| 02CB [🡄] | U+2190 LEFTWARDS ARROW [←]<br/>U+2B05 LEFTWARDS BLACK ARROW [⬅]<br/>U+FFE9 HALFWIDTH LEFTWARDS ARROW [￩]<br/>U+1F844 LEFTWARDS HEAVY ARROW [🡄] |
| 02CC [🡇] | U+2193 DOWNWARDS ARROW [↓]<br/>U+2B07 DOWNWARDS BLACK ARROW [⬇]<br/>U+FFEC HALFWIDTH DOWNWARDS ARROW [￬]<br/>U+1F847 DOWNWARDS HEAVY ARROW [🡇] |
| 0313 [🡅] | U+2191 UPWARDS ARROW [↑]<br/>U+2B06 UPWARDS BLACK ARROW [⬆]<br/>U+FFEA HALFWIDTH UPWARDS ARROW [￪]<br/>U+1F845 UPWARDS HEAVY ARROW [🡅] |

(1) Kanji are not being encoded for now

### English Additions

| Cartridge | Unicode |
| --- | --- |
| 007F [□] | U+25A1 WHITE SQUARE [□] |
| 0080 | N/A |
| 0081 [｢] | U+300C LEFT CORNER BRACKET [「]<br/>U+FF62 HALFWIDTH LEFT CORNER BRACKET [｢] |
| 0082 [｣] | U+300D RIGHT CORNER BRACKET [」]<br/>U+FF63 HALFWIDTH RIGHT CORNER BRACKET [｣] |
| 0083 [○] | U+25CB WHITE CIRCLE [○] |
| 0084 [●] | U+25CF BLACK CIRCLE [●] |
| 0085 [×] | U+00D7 MULTIPLICATION SIGN [×] |
| 0086 [‥] | U+2025 TWO DOT LEADER [‥] |
| 0087 [･] | U+00B7 MIDDLE DOT [·]<br/>U+2022 BULLET [•]<br/>U+30FB KATAKANA MIDDLE DOT [・]<br/>U+FF65 HALFWIDTH KATAKANA MIDDLE DOT [･] |
| 0088 [🡅] | U+2191 UPWARDS ARROW [↑]<br/>U+2B06 UPWARDS BLACK ARROW [⬆]<br/>U+FFEA HALFWIDTH UPWARDS ARROW [￪]<br/>U+1F845 UPWARDS HEAVY ARROW [🡅] |
| 0089 [🡇] | U+2193 DOWNWARDS ARROW [↓]<br/>U+2B07 DOWNWARDS BLACK ARROW [⬇]<br/>U+FFEC HALFWIDTH DOWNWARDS ARROW [￬]<br/>U+1F847 DOWNWARDS HEAVY ARROW [🡇] |
| 008A [🡄] | U+2190 LEFTWARDS ARROW [←]<br/>U+2B05 LEFTWARDS BLACK ARROW [⬅]<br/>U+FFE9 HALFWIDTH LEFTWARDS ARROW [￩]<br/>U+1F844 LEFTWARDS HEAVY ARROW [🡄] |
| 008B [🡆] | U+2192 RIGHTWARDS ARROW [→]<br/>U+2B95 RIGHTWARDS BLACK ARROW [⮕]<br/>U+FFEB HALFWIDTH RIGHTWARDS ARROW [￫]<br/>U+1F846 RIGHTWARDS HEAVY ARROW [🡆] |
| 008C [▼] | U+25BC BLACK DOWN-POINTING TRIANGLE [▼] |
| 008D [♥] | U+2665 BLACK HEART SUIT [♥]<br/>U+2764 HEAVY BLACK HEART [❤] |
| 008E | N/A |
| 008F | N/A (1) |

(1) & is already encoded at 0026 [&]

### French Additions

| Cartridge | Unicode |
| --- | --- |
| 007F [□] | U+25A1 WHITE SQUARE [□] |
| 0080 | N/A |
| 0081 [｢] | U+300C LEFT CORNER BRACKET [「]<br/>U+FF62 HALFWIDTH LEFT CORNER BRACKET [｢] |
| 0082 [｣] | U+300D RIGHT CORNER BRACKET [」]<br/>U+FF63 HALFWIDTH RIGHT CORNER BRACKET [｣] |
| 0083 | N/A (1) |
| 0084 | N/A (1) |
| 0085 | N/A (1) |
| 0086 [‥] | U+2025 TWO DOT LEADER [‥] |
| 0087 [･] | U+00B7 MIDDLE DOT [·]<br/>U+2022 BULLET [•]<br/>U+30FB KATAKANA MIDDLE DOT [・]<br/>U+FF65 HALFWIDTH KATAKANA MIDDLE DOT [･] |
| 0088 [🡅] | U+2191 UPWARDS ARROW [↑]<br/>U+2B06 UPWARDS BLACK ARROW [⬆]<br/>U+FFEA HALFWIDTH UPWARDS ARROW [￪]<br/>U+1F845 UPWARDS HEAVY ARROW [🡅] |
| 0089 [🡇] | U+2193 DOWNWARDS ARROW [↓]<br/>U+2B07 DOWNWARDS BLACK ARROW [⬇]<br/>U+FFEC HALFWIDTH DOWNWARDS ARROW [￬]<br/>U+1F847 DOWNWARDS HEAVY ARROW [🡇] |
| 008A [🡄] | U+2190 LEFTWARDS ARROW [←]<br/>U+2B05 LEFTWARDS BLACK ARROW [⬅]<br/>U+FFE9 HALFWIDTH LEFTWARDS ARROW [￩]<br/>U+1F844 LEFTWARDS HEAVY ARROW [🡄] |
| 008B [🡆] | U+2192 RIGHTWARDS ARROW [→]<br/>U+2B95 RIGHTWARDS BLACK ARROW [⮕]<br/>U+FFEB HALFWIDTH RIGHTWARDS ARROW [￫]<br/>U+1F846 RIGHTWARDS HEAVY ARROW [🡆] |
| 008C [▼] | U+25BC BLACK DOWN-POINTING TRIANGLE [▼] |
| 008D [♥] | U+2665 BLACK HEART SUIT [♥]<br/>U+2764 HEAVY BLACK HEART [❤] |
| 008E [é] | U+00E9 LATIN SMALL LETTER E WITH ACUTE [é] |
| 008F [è] | U+00E8 LATIN SMALL LETTER E WITH GRAVE [è] |
| 0090 [ê] | U+00EA LATIN SMALL LETTER E WITH CIRCUMFLEX [ê] |
| 0091 [ï] | U+00EF LATIN SMALL LETTER I WITH DIAERESIS [ï] |
| 0092 [ù] | U+00F9 LATIN SMALL LETTER U WITH GRAVE [ù] |
| 0093 [à] | U+00E0 LATIN SMALL LETTER A WITH GRAVE [à] |
| 0094 [â] | U+00E2 LATIN SMALL LETTER A WITH CIRCUMFLEX [â] |
| 0095 [î] | U+00EE LATIN SMALL LETTER I WITH CIRCUMFLEX [î] |
| 0096 [ô] | U+00F4 LATIN SMALL LETTER O WITH CIRCUMFLEX [ô] |
| 0097 [û] | U+00FB LATIN SMALL LETTER U WITH CIRCUMFLEX [û] |
| 0098 [ç] | U+00E7 LATIN SMALL LETTER C WITH CEDILLA [ç] |
| 0099 [×] | U+00D7 MULTIPLICATION SIGN [×] |
| 009A | N/A |
| 009B | N/A |
| 009C | N/A |
| 009D | N/A |
| 009E | N/A |
| 009F | N/A |

(1) ê / é / è are already encoded at 0090 [ê] / 008E [é] / 008F [è]

### German Additions

| Cartridge | Unicode |
| --- | --- |
| 007F | N/A |
| 0080 | N/A |
| 0081 [｢] | U+300C LEFT CORNER BRACKET [「]<br/>U+FF62 HALFWIDTH LEFT CORNER BRACKET [｢] |
| 0082 [｣] | U+300D RIGHT CORNER BRACKET [」]<br/>U+FF63 HALFWIDTH RIGHT CORNER BRACKET [｣] |
| 0083 | N/A (1) |
| 0084 | N/A (1) |
| 0085 | N/A (1) |
| 0086 [‥] | U+2025 TWO DOT LEADER [‥] |
| 0087 [･] | U+00B7 MIDDLE DOT [·]<br/>U+2022 BULLET [•]<br/>U+30FB KATAKANA MIDDLE DOT [・]<br/>U+FF65 HALFWIDTH KATAKANA MIDDLE DOT [･] |
| 0088 [🡅] | U+2191 UPWARDS ARROW [↑]<br/>U+2B06 UPWARDS BLACK ARROW [⬆]<br/>U+FFEA HALFWIDTH UPWARDS ARROW [￪]<br/>U+1F845 UPWARDS HEAVY ARROW [🡅] |
| 0089 [🡇] | U+2193 DOWNWARDS ARROW [↓]<br/>U+2B07 DOWNWARDS BLACK ARROW [⬇]<br/>U+FFEC HALFWIDTH DOWNWARDS ARROW [￬]<br/>U+1F847 DOWNWARDS HEAVY ARROW [🡇] |
| 008A [🡄] | U+2190 LEFTWARDS ARROW [←]<br/>U+2B05 LEFTWARDS BLACK ARROW [⬅]<br/>U+FFE9 HALFWIDTH LEFTWARDS ARROW [￩]<br/>U+1F844 LEFTWARDS HEAVY ARROW [🡄] |
| 008B [🡆] | U+2192 RIGHTWARDS ARROW [→]<br/>U+2B95 RIGHTWARDS BLACK ARROW [⮕]<br/>U+FFEB HALFWIDTH RIGHTWARDS ARROW [￫]<br/>U+1F846 RIGHTWARDS HEAVY ARROW [🡆] |
| 008C [▼] | U+25BC BLACK DOWN-POINTING TRIANGLE [▼] |
| 008D [♥] | U+2665 BLACK HEART SUIT [♥]<br/>U+2764 HEAVY BLACK HEART [❤] |
| 008E [Ä] | U+00C4 LATIN CAPITAL LETTER A WITH DIAERESIS [Ä] |
| 008F [ä] | U+00E4 LATIN SMALL LETTER A WITH DIAERESIS [ä] |
| 0090 [Ö] | U+00D6 LATIN CAPITAL LETTER O WITH DIAERESIS [Ö] |
| 0091 [ö] | U+00F6 LATIN SMALL LETTER O WITH DIAERESIS [ö] |
| 0092 [Ü] | U+00DC LATIN CAPITAL LETTER U WITH DIAERESIS [Ü] |
| 0093 [ü] | U+00FC LATIN SMALL LETTER U WITH DIAERESIS [ü] |
| 0094 [ß] | U+00DF LATIN SMALL LETTER SHARP S [ß] |
| 0095 [ẞ] | U+1E9E LATIN CAPITAL LETTER SHARP S [ẞ] |
| 0096 [„] | U+201E DOUBLE LOW-9 QUOTATION MARK [„] |
| 0097 [“] | U+201C LEFT DOUBLE QUOTATION MARK [“] |
| 0098 [●] | U+25CF BLACK CIRCLE [●] |
| 0099 [×] | U+00D7 MULTIPLICATION SIGN [×] |
| 009A | N/A (2) |
| 009B | N/A |
| 009C | N/A |
| 009D | N/A |
| 009E | N/A |
| 009F | N/A |

(1) ä / ö / ü are already encoded at 008F [ä] / 0091 [ö] / 0093 [ü]  
(2) f. does not have a respective unicode codepoint

### Italian Additions

| Cartridge | Unicode |
| --- | --- |
| 005E | N/A (1) |
| 005F […] | U+2026 HORIZONTAL ELLIPSIS […] |
| 0060 | N/A |
| 007F [‟] | U+201F DOUBLE HIGH-REVERSED-9 QUOTATION MARK [‟] |
| 0080 [à] | U+00E0 LATIN SMALL LETTER A WITH GRAVE [à] |
| 0081 [è] | U+00E8 LATIN SMALL LETTER E WITH GRAVE [è] |
| 0082 [é] | U+00E9 LATIN SMALL LETTER E WITH ACUTE [é] |
| 0083 [ì] | U+00EC LATIN SMALL LETTER I WITH GRAVE [ì] |
| 0084 [ò] | U+00F2 LATIN SMALL LETTER O WITH GRAVE [ò] |
| 0085 [ù] | U+00F9 LATIN SMALL LETTER U WITH GRAVE [ù] |
| 0086 | N/A |
| 0087 | N/A |
| 0088 [À] | U+00C0 LATIN CAPITAL LETTER A WITH GRAVE [À] |
| 0089 [È] | U+00C8 LATIN CAPITAL LETTER E WITH GRAVE [È] |
| 008A [É] | U+00C9 LATIN CAPITAL LETTER E WITH ACUTE [É] |
| 008B [Ì] | U+00CC LATIN CAPITAL LETTER I WITH GRAVE [Ì] |
| 008C [Ò] | U+00D2 LATIN CAPITAL LETTER O WITH GRAVE [Ò] |
| 008D [Ù] | U+00D9 LATIN CAPITAL LETTER U WITH GRAVE [Ù] |
| 008E | N/A |
| 008F [¿] | U+00BF INVERTED QUESTION MARK [¿] |
| 0090 [¡] | U+00A1 INVERTED EXCLAMATION MARK [¡] |
| 0091 [｢] | U+300C LEFT CORNER BRACKET [「]<br/>U+FF62 HALFWIDTH LEFT CORNER BRACKET [｢] |
| 0092 [｣] | U+300D RIGHT CORNER BRACKET [」]<br/>U+FF63 HALFWIDTH RIGHT CORNER BRACKET [｣] |
| 0093 [○] | U+25CB WHITE CIRCLE [○] |
| 0094 [●] | U+25CF BLACK CIRCLE [●] |
| 0095 [×] | U+00D7 MULTIPLICATION SIGN [×] |
| 0096 | N/A |
| 0097 [‥] | U+2025 TWO DOT LEADER [‥] |
| 0098 | N/A |
| 0099 [･] | U+00B7 MIDDLE DOT [·]<br/>U+2022 BULLET [•]<br/>U+30FB KATAKANA MIDDLE DOT [・]<br/>U+FF65 HALFWIDTH KATAKANA MIDDLE DOT [･] |
| 009A [🡅] | U+2191 UPWARDS ARROW [↑]<br/>U+2B06 UPWARDS BLACK ARROW [⬆]<br/>U+FFEA HALFWIDTH UPWARDS ARROW [￪]<br/>U+1F845 UPWARDS HEAVY ARROW [🡅] |
| 009B [🡇] | U+2193 DOWNWARDS ARROW [↓]<br/>U+2B07 DOWNWARDS BLACK ARROW [⬇]<br/>U+FFEC HALFWIDTH DOWNWARDS ARROW [￬]<br/>U+1F847 DOWNWARDS HEAVY ARROW [🡇] |
| 009C [🡄] | U+2190 LEFTWARDS ARROW [←]<br/>U+2B05 LEFTWARDS BLACK ARROW [⬅]<br/>U+FFE9 HALFWIDTH LEFTWARDS ARROW [￩]<br/>U+1F844 LEFTWARDS HEAVY ARROW [🡄] |
| 009D [🡆] | U+2192 RIGHTWARDS ARROW [→]<br/>U+2B95 RIGHTWARDS BLACK ARROW [⮕]<br/>U+FFEB HALFWIDTH RIGHTWARDS ARROW [￫]<br/>U+1F846 RIGHTWARDS HEAVY ARROW [🡆] |
| 009E [▼] | U+25BC BLACK DOWN-POINTING TRIANGLE [▼] |
| 009F [♥] | U+2665 BLACK HEART SUIT [♥]<br/>U+2764 HEAVY BLACK HEART [❤] |

(1) ll does not have a respective unicode codepoint

### Spanish Additions

| Cartridge | Unicode |
| --- | --- |
| 005B [Á] | U+00C1 LATIN CAPITAL LETTER A WITH ACUTE [Á] |
| 005C [É] | U+00C9 LATIN CAPITAL LETTER E WITH ACUTE [É] |
| 005D [Í] | U+00CD LATIN CAPITAL LETTER I WITH ACUTE [Í] |
| 005E [Ó] | U+00D3 LATIN CAPITAL LETTER O WITH ACUTE [Ó] |
| 005F [Ú] | U+00DA LATIN CAPITAL LETTER U WITH ACUTE [Ú] |
| 0060 [Ü] | U+00DC LATIN CAPITAL LETTER U WITH DIAERESIS [Ü] |
| 0061 [Ñ] | U+00D1 LATIN CAPITAL LETTER N WITH TILDE [Ñ] |
| 0062 [Ç] | U+00C7 LATIN CAPITAL LETTER C WITH CEDILLA [Ç] |
| 0063 [[] | U+005B LEFT SQUARE BRACKET [[]<br/>U+FF3B FULLWIDTH LEFT SQUARE BRACKET [［] |
| 0064 [\\] | U+005C REVERSE SOLIDUS [\\]<br/>U+FF3C FULLWIDTH REVERSE SOLIDUS [＼] |
| 0065 []] | U+005D RIGHT SQUARE BRACKET []]<br/>U+FF3D FULLWIDTH RIGHT SQUARE BRACKET [］] |
| 0066 | N/A (1) |
| 0067 […] | U+2026 HORIZONTAL ELLIPSIS […] |
| 0068 [‟] | U+201F DOUBLE HIGH-REVERSED-9 QUOTATION MARK [‟] |
| 0069 [a] | U+0061 LATIN SMALL LETTER A [a]<br/>U+FF41 FULLWIDTH LATIN SMALL LETTER A [ａ] |
| 006A [b] | U+0062 LATIN SMALL LETTER B [b]<br/>U+FF42 FULLWIDTH LATIN SMALL LETTER B [ｂ] |
| 006B [c] | U+0063 LATIN SMALL LETTER C [c]<br/>U+FF43 FULLWIDTH LATIN SMALL LETTER C [ｃ] |
| 006C [d] | U+0064 LATIN SMALL LETTER D [d]<br/>U+FF44 FULLWIDTH LATIN SMALL LETTER D [ｄ] |
| 006D [e] | U+0065 LATIN SMALL LETTER E [e]<br/>U+FF45 FULLWIDTH LATIN SMALL LETTER E [ｅ] |
| 006E [f] | U+0066 LATIN SMALL LETTER F [f]<br/>U+FF46 FULLWIDTH LATIN SMALL LETTER F [ｆ] |
| 006F [g] | U+0067 LATIN SMALL LETTER G [g]<br/>U+FF47 FULLWIDTH LATIN SMALL LETTER G [ｇ] |
| 0070 [h] | U+0068 LATIN SMALL LETTER H [h]<br/>U+FF48 FULLWIDTH LATIN SMALL LETTER H [ｈ] |
| 0071 [i] | U+0069 LATIN SMALL LETTER I [i]<br/>U+FF49 FULLWIDTH LATIN SMALL LETTER I [ｉ] |
| 0072 [j] | U+006A LATIN SMALL LETTER J [j]<br/>U+FF4A FULLWIDTH LATIN SMALL LETTER J [ｊ] |
| 0073 [k] | U+006B LATIN SMALL LETTER K [k]<br/>U+FF4B FULLWIDTH LATIN SMALL LETTER K [ｋ] |
| 0074 [l] | U+006C LATIN SMALL LETTER L [l]<br/>U+FF4C FULLWIDTH LATIN SMALL LETTER L [ｌ] |
| 0075 [m] | U+006D LATIN SMALL LETTER M [m]<br/>U+FF4D FULLWIDTH LATIN SMALL LETTER M [ｍ] |
| 0076 [n] | U+006E LATIN SMALL LETTER N [n]<br/>U+FF4E FULLWIDTH LATIN SMALL LETTER N [ｎ] |
| 0077 [o] | U+006F LATIN SMALL LETTER O [o]<br/>U+FF4F FULLWIDTH LATIN SMALL LETTER O [ｏ] |
| 0078 [p] | U+0070 LATIN SMALL LETTER P [p]<br/>U+FF50 FULLWIDTH LATIN SMALL LETTER P [ｐ] |
| 0079 [q] | U+0071 LATIN SMALL LETTER Q [q]<br/>U+FF51 FULLWIDTH LATIN SMALL LETTER Q [ｑ] |
| 007A [r] | U+0072 LATIN SMALL LETTER R [r]<br/>U+FF52 FULLWIDTH LATIN SMALL LETTER R [ｒ] |
| 007B [s] | U+0073 LATIN SMALL LETTER S [s]<br/>U+FF53 FULLWIDTH LATIN SMALL LETTER S [ｓ] |
| 007C [t] | U+0074 LATIN SMALL LETTER T [t]<br/>U+FF54 FULLWIDTH LATIN SMALL LETTER T [ｔ] |
| 007D [u] | U+0075 LATIN SMALL LETTER U [u]<br/>U+FF55 FULLWIDTH LATIN SMALL LETTER U [ｕ] |
| 007E [v] | U+0076 LATIN SMALL LETTER V [v]<br/>U+FF56 FULLWIDTH LATIN SMALL LETTER V [ｖ] |
| 007F [w] | U+0077 LATIN SMALL LETTER W [w]<br/>U+FF57 FULLWIDTH LATIN SMALL LETTER W [ｗ] |
| 0080 [x] | U+0078 LATIN SMALL LETTER X [x]<br/>U+FF58 FULLWIDTH LATIN SMALL LETTER X [ｘ] |
| 0081 [y] | U+0079 LATIN SMALL LETTER Y [y]<br/>U+FF59 FULLWIDTH LATIN SMALL LETTER Y [ｙ] |
| 0082 [z] | U+007A LATIN SMALL LETTER Z [z]<br/>U+FF5A FULLWIDTH LATIN SMALL LETTER Z [ｚ] |
| 0083 [á] | U+00E1 LATIN SMALL LETTER A WITH ACUTE [á] |
| 0084 [é] | U+00E9 LATIN SMALL LETTER E WITH ACUTE [é] |
| 0085 [í] | U+00ED LATIN SMALL LETTER I WITH ACUTE [í] |
| 0086 [ó] | U+00F3 LATIN SMALL LETTER O WITH ACUTE [ó] |
| 0087 [ú] | U+00FA LATIN SMALL LETTER U WITH ACUTE [ú] |
| 0088 [ü] | U+00FC LATIN SMALL LETTER U WITH DIAERESIS [ü] |
| 0089 [ñ] | U+00F1 LATIN SMALL LETTER N WITH TILDE [ñ] |
| 008A [ç] | U+00E7 LATIN SMALL LETTER C WITH CEDILLA [ç] |
| 008B [{] | U+007B LEFT CURLY BRACKET [{]<br/>U+FF5B FULLWIDTH LEFT CURLY BRACKET [｛] |
| 008C [¦] | U+007C VERTICAL LINE [\|]<br/>U+00A6 BROKEN BAR [¦]<br/>U+FF5C FULLWIDTH VERTICAL LINE [｜]<br/>U+FFE4 FULLWIDTH BROKEN BAR [￤] |
| 008D [}] | U+007D RIGHT CURLY BRACKET [}]<br/>U+FF5D FULLWIDTH RIGHT CURLY BRACKET [｝] |
| 008E [˜] | U+007E TILDE [~]<br/>U+02DC SMALL TILDE [˜]<br/>U+FF5E FULLWIDTH TILDE [～] |
| 008F [¿] | U+00BF INVERTED QUESTION MARK [¿] |
| 0090 [¡] | U+00A1 INVERTED EXCLAMATION MARK [¡] |
| 0091 [｢] | U+300C LEFT CORNER BRACKET [「]<br/>U+FF62 HALFWIDTH LEFT CORNER BRACKET [｢] |
| 0092 [｣] | U+300D RIGHT CORNER BRACKET [」]<br/>U+FF63 HALFWIDTH RIGHT CORNER BRACKET [｣] |
| 0093 [○] | U+25CB WHITE CIRCLE [○] |
| 0094 [●] | U+25CF BLACK CIRCLE [●] |
| 0095 [×] | U+00D7 MULTIPLICATION SIGN [×] |
| 0096 | N/A |
| 0097 [‥] | U+2025 TWO DOT LEADER [‥] |
| 0098 | N/A |
| 0099 [･] | U+00B7 MIDDLE DOT [·]<br/>U+2022 BULLET [•]<br/>U+30FB KATAKANA MIDDLE DOT [・]<br/>U+FF65 HALFWIDTH KATAKANA MIDDLE DOT [･] |
| 009A [🡅] | U+2191 UPWARDS ARROW [↑]<br/>U+2B06 UPWARDS BLACK ARROW [⬆]<br/>U+FFEA HALFWIDTH UPWARDS ARROW [￪]<br/>U+1F845 UPWARDS HEAVY ARROW [🡅] |
| 009B [🡇] | U+2193 DOWNWARDS ARROW [↓]<br/>U+2B07 DOWNWARDS BLACK ARROW [⬇]<br/>U+FFEC HALFWIDTH DOWNWARDS ARROW [￬]<br/>U+1F847 DOWNWARDS HEAVY ARROW [🡇] |
| 009C [🡄] | U+2190 LEFTWARDS ARROW [←]<br/>U+2B05 LEFTWARDS BLACK ARROW [⬅]<br/>U+FFE9 HALFWIDTH LEFTWARDS ARROW [￩]<br/>U+1F844 LEFTWARDS HEAVY ARROW [🡄] |
| 009D [🡆] | U+2192 RIGHTWARDS ARROW [→]<br/>U+2B95 RIGHTWARDS BLACK ARROW [⮕]<br/>U+FFEB HALFWIDTH RIGHTWARDS ARROW [￫]<br/>U+1F846 RIGHTWARDS HEAVY ARROW [🡆] |
| 009E [▼] | U+25BC BLACK DOWN-POINTING TRIANGLE [▼] |
| 009F [♥] | U+2665 BLACK HEART SUIT [♥]<br/>U+2764 HEAVY BLACK HEART [❤] |

(1) ll does not have a respective unicode codepoint

## Appendix A: Comparison of All Characters by Language

This is a list of all characters in the range from 0020 to 009F by language as they appear in-game.

**Remarks**

- Problematic characters are marked with a red square. They are exempt from encoding.
- Japanese uses fullwidth characters.
- Slected characters of the Japanese encoding beyond 009F are listed separatedly.
- Furthermore, Japanese kana and kanji are listed as N/A.

| | Japanese | English | German | French | Italian | Spanish |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 0020 | 　 |   |   |   |   |   |
| 0021 | ！ | ! | ! | ! | ! | ! |
| 0022 | ” | " | " | " | " | " |
| 0023 | “ | # | # | # | # | # |
| 0024 | ▼ | $ | $ | $ | $ | $ |
| 0025 | ％ | % | % | % | % | % |
| 0026 | ‘ | & | & | & | & | & |
| 0027 | ’ | ' | ' | ' | ' | ' |
| 0028 | （ | ( | ( | ( | ( | ( |
| 0029 | ） | ) | ) | ) | ) | ) |
| 002A | ＊ | ∗ | ∗ | ∗ | ∗ | ∗ |
| 002B | ＋ | + | + | + | + | + |
| 002C | ， | , | , | , | , | , |
| 002D | － | − | − | − | − | − |
| 002E | ． | . | . | . | . | . |
| 002F | ／ | / | / | / | / | / |
| 0030 | ０ | 0 | 0 | 0 | 0 | 0 |
| 0031 | １ | 1 | 1 | 1 | 1 | 1 |
| 0032 | ２ | 2 | 2 | 2 | 2 | 2 |
| 0033 | ３ | 3 | 3 | 3 | 3 | 3 |
| 0034 | ４ | 4 | 4 | 4 | 4 | 4 |
| 0035 | ５ | 5 | 5 | 5 | 5 | 5 |
| 0036 | ６ | 6 | 6 | 6 | 6 | 6 |
| 0037 | ７ | 7 | 7 | 7 | 7 | 7 |
| 0038 | ８ | 8 | 8 | 8 | 8 | 8 |
| 0039 | ９ | 9 | 9 | 9 | 9 | 9 |
| 003A | ： | : | : | : | : | : |
| 003B | 「 | ; | ; | ; | ; | ; |
| 003C | 」 | < | < | < | < | < |
| 003D | ＝ | = | = | = | = | = |
| 003E | ○ | > | > | > | > | > |
| 003F | ？ | ? | ? | ? | ? | ? |
| 0040 | ● | @ | @ | @ | @ | @ |
| 0041 | Ａ | A | A | A | A | A |
| 0042 | Ｂ | B | B | B | B | B |
| 0043 | Ｃ | C | C | C | C | C |
| 0044 | Ｄ | D | D | D | D | D |
| 0045 | Ｅ | E | E | E | E | E |
| 0046 | Ｆ | F | F | F | F | F |
| 0047 | Ｇ | G | G | G | G | G |
| 0048 | Ｈ | H | H | H | H | H |
| 0049 | Ｉ | I | I | I | I | I |
| 004A | Ｊ | J | J | J | J | J |
| 004B | Ｋ | K | K | K | K | K |
| 004C | Ｌ | L | L | L | L | L |
| 004D | Ｍ | M | M | M | M | M |
| 004E | Ｎ | N | N | N | N | N |
| 004F | Ｏ | O | O | O | O | O |
| 0050 | Ｐ | P | P | P | P | P |
| 0051 | Ｑ | Q | Q | Q | Q | Q |
| 0052 | Ｒ | R | R | R | R | R |
| 0053 | Ｓ | S | S | S | S | S |
| 0054 | Ｔ | T | T | T | T | T |
| 0055 | Ｕ | U | U | U | U | U |
| 0056 | Ｖ | V | V | V | V | V |
| 0057 | Ｗ | W | W | W | W | W |
| 0058 | Ｘ | X | X | X | X | X |
| 0059 | Ｙ | Y | Y | Y | Y | Y |
| 005A | Ｚ | Z | Z | Z | Z | Z |
| 005B | × | [ | [ | [ | [ | Á |
| 005C | … | \ | \ | \ | \ | É |
| 005D | N/A | ] | ] | ] | ] | Í |
| 005E | N/A | ^ | ^ | ^ | ll 🟥 | Ó |
| 005F | N/A | _ | _ | _ | … | Ú |
| 0060 | ～ | \` | \` | \` |  | Ü |
| 0061 | ａ | a | a | a | a | Ñ |
| 0062 | ｂ | b | b | b | b | Ç |
| 0063 | ｃ | c | c | c | c | [ |
| 0064 | ｄ | d | d | d | d | \ |
| 0065 | ｅ | e | e | e | e | } |
| 0066 | ｆ | f | f | f | f | ll 🟥 |
| 0067 | ｇ | g | g | g | g | … |
| 0068 | ｈ | h | h | h | h | ‟ |
| 0069 | ｉ | i | i | i | i | a |
| 006A | ｊ | j | j | j | j | b |
| 006B | ｋ | k | k | k | k | c |
| 006C | ｌ | l | l | l | l | d |
| 006D | ｍ | m | m | m | m | e |
| 006E | ｎ | n | n | n | n | f |
| 006F | ｏ | o | o | o | o | g |
| 0070 | ｐ | p | p | p | p | h |
| 0071 | ｑ | q | q | q | q | i |
| 0072 | ｒ | r | r | r | r | j |
| 0073 | ｓ | s | s | s | s | k |
| 0074 | ｔ | t | t | t | t | l |
| 0075 | ｕ | u | u | u | u | m |
| 0076 | ｖ | v | v | v | v | n |
| 0077 | ｗ | w | w | w | w | o |
| 0078 | ｘ | x | x | x | x | p |
| 0079 | ｙ | y | y | y | y | q |
| 007A | ｚ | z | z | z | z | r |
| 007B | 、 | { | { | { | { | s |
| 007C | 。 | ¦ | ¦ | ¦ | ¦ | t |
| 007D | ー | } | } | } | } | u |
| 007E | ♥ | ˜ | ˜ | ˜ | ˜ | v |
| 007F | N/A | □ |  | □ | ‟ | w |
| 0080 | N/A |  |  |  | à | x |
| 0081 | N/A | ｢ | ｢ | ｢ | è | y |
| 0082 | N/A | ｣ | ｣ | ｣ | é | z |
| 0083 | N/A | ○ | ä 🟥 | ê 🟥 | ì | á |
| 0084 | N/A | ● | ö 🟥 | é 🟥 | ò | é |
| 0085 | N/A | × | ü 🟥 | è 🟥 | ù | í |
| 0086 | N/A | ‥ | ‥ | ‥ |  | ó |
| 0087 | N/A | ･ | ･ | ･ |  | ú |
| 0088 | N/A | 🡅 | 🡅 | 🡅 | À | ü |
| 0089 | N/A | 🡇 | 🡇 | 🡇 | È | ñ |
| 008A | N/A | 🡄 | 🡄 | 🡄 | É | ç |
| 008B | N/A | 🡆 | 🡆 | 🡆 | Ì | { |
| 008C | N/A | ▼ | ▼ | ▼ | Ò | ¦ |
| 008D | N/A | ♥ | ♥ | ♥ | Ù | } |
| 008E | N/A |  | Ä | é |  | ˜ |
| 008F | N/A | & 🟥 | ä | è | ¿ | ¿ |
| 0090 | N/A |  | Ö | ê | ¡ | ¡ |
| 0091 | N/A |  | ö | ï | ｢ | ｢ |
| 0092 | N/A |  | Ü | ù | ｣ | ｣ |
| 0093 | N/A |  | ü | à | ○ | ○ |
| 0094 | N/A |  | ß | â | ● | ● |
| 0095 | N/A |  | ẞ | î | × | × |
| 0096 | N/A |  | „ | ô |  |  |
| 0097 | N/A |  | “ | û | ‥ | ‥ |
| 0098 | N/A |  | ● | ç |  |  |
| 0099 | N/A |  | × | × | ･ | ･ |
| 009A | N/A |  | f. 🟥 |  | 🡅 | 🡅 |
| 009B | N/A |  |  |  | 🡇 | 🡇 |
| 009C | N/A |  |  |  | 🡄 | 🡄 |
| 009D | N/A |  |  |  | 🡆 | 🡆 |
| 009E | N/A |  |  |  | ▼ | ▼ |
| 009F | N/A |  |  |  | ♥ | ♥ |

| | Japanese |
| :---: | :---: |
| 0120 | 『 |
| 012B | ＿ |
| 0163 | 』 |
| 01AF | ・ |
| 020F | 🡆 |
| 0245 | 【 |
| 0246 | 】 |
| 0290 | ［ |
| 0291 | ］ |
| 02CB | 🡄 |
| 02CC | 🡇 |
| 0313 | 🡅 |

## Appendix B: Name Selection Screens

These are the in-game name selection screens for each language version.

### Japanese

| | | | | | | | | | | | | | | | | | | | | |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| あ | い | う | え | お | ら | り | る | れ | ろ | ア | イ | ウ | エ | オ | ラ | リ | ル | レ | ロ | ヴ |
| か | き | く | け | こ | が | ぎ | ぐ | げ | ご | カ | キ | ク | ケ | コ | ガ | ギ | グ | ゲ | ゴ | ー |
| さ | し | す | せ | そ | ざ | じ | ず | ぜ | ぞ | サ | シ | ス | セ | ソ | ザ | ジ | ズ | ゼ | ゾ | ～ |
| た | ち | つ | て | と | だ | ぢ | づ | で | ど | タ | チ | ツ | テ | ト | ダ | ヂ | ヅ | デ | ド | … |
| な | に | ぬ | ね | の | ば | び | ぶ | べ | ぼ | ナ | ニ | ヌ | ネ | ノ | バ | ビ | ブ | ベ | ボ | ・ |
| は | ひ | ふ | へ | ほ | ぱ | ぴ | ぷ | ぺ | ぽ | ハ | ヒ | フ | ヘ | ホ | パ | ピ | プ | ペ | ポ | ！ |
| ま | み | む | め | も | ぁ | ぃ | ぅ | ぇ | ぉ | マ | ミ | ム | メ | モ | ァ | ィ | ゥ | ェ | ォ | ？ |
| や | ゆ | よ | わ | ん | ゃ | ゅ | ょ | っ | を | ヤ | ユ | ヨ | ワ | ン | ャ | ュ | ョ | ッ | ヲ | ▼ |

Note that the downwards triangle functions as the confirmation button.

### English

| | | | | | | | | | | | | |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| A | B | C | D | E | F | G | H | I | J | K | L | M |
| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| a | b | c | d | e | f | g | h | i | j | k | l | m |
| n | o | p | q | r | s | t | u | v | w | x | y | z |
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | . | ! | ? |
| & | : | + | − | ∗ | / | = | ( | ) | " | ' | , | &nbsp; |
| % | _ | 🡅 | 🡇 | 🡄 | 🡆 | ♥ | [ | ] | ˜ | × | ○ | ● |

### German

| | | | | | | | | | | | | |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| A | B | C | D | E | F | G | H | I | J | K | L | M |
| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| a | b | c | d | e | f | g | h | i | j | k | l | m |
| n | o | p | q | r | s | t | u | v | w | x | y | z |
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | &nbsp; | . | ' |
| Ä | Ö | Ü | ẞ | ä | ö | ü | ß | + | − | ∗ | : | # |
| ( | ) | { | } | [ | ] | < | > | 🡅 | 🡇 | 🡄 | 🡆 | ♥ |

### French

| | | | | | | | | | | | | |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| A | B | C | D | E | F | G | H | I | J | K | L | M |
| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| a | b | c | d | e | f | g | h | i | j | k | l | m |
| n | o | p | q | r | s | t | u | v | w | x | y | z |
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | ( | ) | ' |
| é | è | ê | ï | ù | à | â | î | ô | û | ç | &nbsp; | &nbsp; |
| % | _ | 🡅 | 🡇 | 🡄 | 🡆 | ♥ | [ | ] | ˜ | &nbsp; | &nbsp; | &nbsp; |

### Italian

| | | | | | | | | | | | | |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| A | B | C | D | E | F | G | H | I | J | K | L | M |
| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| a | b | c | d | e | f | g | h | i | j | k | l | m |
| n | o | p | q | r | s | t | u | v | w | x | y | z |
| À | È | É | Ì | Ò | Ù | ll | à | è | é | ì | ò | ù |
| + | − | = | ∗ | & | % | $ | # | , | . | ( | ) | &nbsp; |
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | &nbsp; | &nbsp; | &nbsp; |

### Spanish

| | | | | | | | | | | | | |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| A | B | C | D | E | F | G | H | I | J | K | L | M |
| N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
| a | b | c | d | e | f | g | h | i | j | k | l | m |
| n | o | p | q | r | s | t | u | v | w | x | y | z |
| Á | É | Í | Ó | Ú | Ü | Ñ | Ç | á | é | í | ó | ú |
| ü | ñ | ç | + | − | = | ∗ | & | % | $ | # | , | . |
| ( | ) | &nbsp; | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |

