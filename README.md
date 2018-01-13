# ***WIP!***
All themes this repository provides will be likely to change.

# lem-pygments-colorthemes
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/koji-kojiro/lem-pygments-colorthemes/blob/master/LICENSE)
[![Quicklisp dist](http://quickdocs.org/badge/lem-pygments-colorthemes.svg)](http://quickdocs.org/lem-pygments-colorthemes/)<br>

Color themes for [lem](https://github.com/cxxxr/lem) ported from [pygments](http://pygments.org/)<br>

<br>
<p align="center">
  <img src="https://github.com/koji-kojiro/lem-pygments-colorthemes/blob/master/sample/monokai.png">
</p>


## Installation
Via Roswell.<br>

```
$ ros install koji-kojiro/lem-pygments-colorthemes
```

And edit your `.lemrc` as follows.<br>

```common-lisp
(load-library "pygments-colorthemes")
(load-theme "monokai")
```

[Available themes](./themes)<br>
Note that the compatibility is incomplete due to the difference between lem and pygments.

## License
Licensed under [MIT License](LICENSE).

## Author
[TANI Kojiro](https://github.com/koji-kojiro) (kojiro0531@gmail.com)
