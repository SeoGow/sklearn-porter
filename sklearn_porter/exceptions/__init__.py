# -*- coding: utf-8 -*-

from sklearn_porter.enums import Language, Method, Template


class SklearnPorterError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class NotFittedEstimatorError(SklearnPorterError):
    def __init__(self, message: str):
        hint = 'The passed estimator of kind `{}` ' \
               'is not fitted.'.format(message)
        self.message = hint
        super().__init__(self.message)


class NotSupportedError(SklearnPorterError):
    def __init__(self, message: str):
        hint = 'You can check the documentation ' \
               'or create a new feature request at ' \
               'https://github.com/nok/sklearn-porter .'
        self.message = message + '\n' + hint
        super().__init__(self.message)


class InvalidMethodError(SklearnPorterError):
    def __init__(self, message: str):
        opts = ', '.join(['`{}`'.format(m.value) for m in list(Method)])
        hint = 'The passed method `{}` is invalid. ' \
               'Valid methods are: {}.'.format(message, opts)
        self.message = hint
        super().__init__(self.message)


class InvalidLanguageError(SklearnPorterError):
    def __init__(self, message: str):
        opts = ', '.join(['`{}`'.format(l.value.KEY) for l in list(Language)])
        hint = 'The passed language `{}` is invalid. ' \
               'Valid languages are: {}.'.format(message, opts)
        self.message = hint
        super().__init__(self.message)


class InvalidTemplateError(SklearnPorterError):
    def __init__(self, message: str):
        opts = ', '.join(['`{}`'.format(t.value) for t in list(Template)])
        hint = 'The passed template `{}` is invalid. ' \
               'Valid templates are: {}.'.format(message, opts)
        self.message = hint
        super().__init__(self.message)