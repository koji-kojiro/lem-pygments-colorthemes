(in-package :lem-user)

(define-color-theme "vs" ()
  (foreground "#000000")
  (background "#ffffff")
  (cursor :foreground "#ffffff" :background "#000000")
  (syntax-warning-attribute :foreground nil :background "#ffffff")
  (syntax-string-attribute :foreground "#af0000" :background "#ffffff")
  (syntax-comment-attribute :foreground "#008000" :background "#ffffff")
  (syntax-keyword-attribute :foreground "#0000ff" :background "#ffffff")
  (syntax-constant-attribute :foreground nil :background "#ffffff")
  (syntax-function-name-attribute :foreground nil :background "#ffffff")
  (syntax-variable-attribute :foreground nil :background "#ffffff")
  (syntax-type-attribute :foreground "#0087af" :background "#ffffff")
  (syntax-builtin-attribute :foreground nil :background "#ffffff"))
