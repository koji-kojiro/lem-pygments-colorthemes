(in-package :lem-user)

(define-color-theme "pastie" ()
  (foreground "#000000")
  (background "#ffffff")
  (cursor :foreground "#ffffff" :background "#000000")
  (syntax-warning-attribute :foreground "#af0000" :background "#ffffff")
  (syntax-string-attribute :foreground "#d70000" :background "#ffffff")
  (syntax-comment-attribute :foreground "#878787" :background "#ffffff")
  (syntax-keyword-attribute :foreground "#008700" :background "#ffffff")
  (syntax-constant-attribute :foreground "#005f5f" :background "#ffffff")
  (syntax-function-name-attribute :foreground "#005faf" :background "#ffffff")
  (syntax-variable-attribute :foreground "#5f5f87" :background "#ffffff")
  (syntax-type-attribute :foreground "#878787" :background "#ffffff")
  (syntax-builtin-attribute :foreground "#005f87" :background "#ffffff"))
