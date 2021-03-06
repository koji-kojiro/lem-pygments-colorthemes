(in-package :lem-user)

(define-color-theme "friendly" ()
  (foreground "#000000")
  (background "#eeeeee")
  (cursor :foreground "#eeeeee" :background "#000000")
  (syntax-warning-attribute :foreground nil :background "#eeeeee")
  (syntax-string-attribute :foreground "#5f5faf" :background "#eeeeee")
  (syntax-comment-attribute :foreground "#5fafaf" :background "#eeeeee")
  (syntax-keyword-attribute :foreground "#008000" :background "#eeeeee")
  (syntax-constant-attribute :foreground "#5fafd7" :background "#eeeeee")
  (syntax-function-name-attribute :foreground "#000080" :background "#eeeeee")
  (syntax-variable-attribute :foreground "#af5fd7" :background "#eeeeee")
  (syntax-type-attribute :foreground "#870000" :background "#eeeeee")
  (syntax-builtin-attribute :foreground "#008000" :background "#eeeeee"))
