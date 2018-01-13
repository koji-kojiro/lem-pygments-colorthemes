(in-package :lem-user)

(define-color-theme "vim" ()
  (foreground "#ffffff")
  (background "#000000")
  (syntax-warning-attribute :foreground nil)
  (syntax-string-attribute :foreground "#cd0000")
  (syntax-comment-attribute :foreground "#000080")
  (syntax-keyword-attribute :foreground "#cdcd00")
  (syntax-constant-attribute :foreground nil)
  (syntax-function-name-attribute :foreground nil)
  (syntax-variable-attribute :foreground "#00cdcd")
  (syntax-type-attribute :foreground "#00cd00")
  (syntax-builtin-attribute :foreground "#cd00cd"))
