��������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������������s.closeHtml);
                var progressBar = {
                    intervalId: null,
                    hideEta: null,
                    maxHideTime: null
                };
                var response = {
                    toastId: toastId,
                    state: 'visible',
                    startTime: new Date(),
                    options: options,
                    map: map
                };

                personalizeToast();

                displayToast();

                handleEvents();

                publish(response);

                if (options.debug && console) {
                    console.log(response);
                }

                return $toastElement;

                function escapeHtml(source) {
                    if (source == null) {
                        source = '';
                    }

                    return source
                        .replace(/&/g, '&amp;')
                        .replace(/"/g, '&quot;')
                        .replace(/'/g, '&#39;')
                        .replace(/</g, '&lt;')
                        .replace(/>/g, '&gt;');
                }

                function personalizeToast() {
                    setIcon();
                    setTitle();
                    setMessage();
                    setCloseButton();
                    setProgressBar();
                    setRTL();
                    setSequence();
                    setAria();
                }

                function setAria() {
                    var ariaValue = '';
                    switch (map.iconClass) {
                        case 'toast-success':
                        case 'toast-info':
                            ariaValue =  'polite';
                            break;
                        default:
                            ariaValue = 'assertive';
                    }
                    $toastElement.attr('aria-live', ariaValue);
                }

                function handleEvents() {
                    if (options.closeOnHover) {
                        $toastElement.hover(stickAround, delayedHideToast);
                    }

                    if (!options.onclick && options.tapToDismiss) {
                        $toastElement.click(hideToast);
                    }

                    if (options.closeButton && $closeElement) {
                        $closeElement.click(function (event) {
                            if (event.stopPropagation) {
                                event.stopPropagation();
                            } else if (event.cancelBubble !== undefined && event.cancelBubble !== true) {
                                event.cancelBubble = true;
                            }

                            if (options.onCloseClick) {
                                options.onCloseClick(event);
                            }

                            hideToast(true);
                        });
                    }

                    if (options.onclick) {
                        $toastElement.click(function (event) {
                            options.onclick(event);
                            hideToast();
                        });
                    }
                }

                function displayToast() {
                    $toastElement.hide();

                    $toastElement[options.showMethod](
                        {duration: options.showDuration, easing: options.showEasing, complete: options.onShown}
                    );

                    if (options.timeOut > 0) {
                        intervalId = setTimeout(hideToast, options.timeOut);
                        progressBar.maxHideTime = parseFloat(options.timeOut);
                        progressBar.hideEta = new Date().getTime() + progressBar.maxHideTime;
                        if (options.progressBar) {
                            progressBar.intervalId = setInterval(updateProgress, 10);
                        }
                    }
                }

                function setIcon() {
                    if (map.iconClass) {
                        $toastElement.addClass(options.toastClass).addClass(iconClass);
                    }
                }

                function setSequence() {
                    if (options.newestOnTop) {
                        $container.prepend($toastElement);
                    } else {
                        $container.append($toastElement);
                    }
                }

                function setTitle() {
                    if (map.title) {
                        var suffix = map.title;
                        if (options.escapeHtml) {
                            suffix = escapeHtml(map.title);
                        }
                        $titleElement.append(suffix).addClass(options.titleClass);
                        $toastElement.append($titleElement);
                    }
                }

                function setMessage() {
                    if (map.message) {
                        var suffix = map.message;
                        if (options.escapeHtml) {
                            suffix = escapeHtml(map.message);
                        }
                        $messageElement.append(suffix).addClass(options.messageClass);
                        $toastElement.append($messageElement);
                    }
                }

                function setCloseButton() {
                    if (options.closeButton) {
                        $closeElement.addClass(options.closeClass).attr('role', 'button');
                        $toastElement.prepend($closeElement);
                    }
                }

                function setProgressBar() {
                    if (options.progressBar) {
                        $progressElement.addClass(options.progressClass);
                        $toastElement.prepend($progressElement);
                    }
                }

                function setRTL() {
                    if (options.rtl) {
                        $toastElement.addClass('rtl');
                    }
                }

                function shouldExit(options, map) {
                    if (options.preventDuplicates) {
                        if (map.message === previousToast) {
                            return true;
                        } else {
                            previousToast = map.message;
                        }
                    }
                    return false;
                }

                function hideToast(override) {
                    var method = override && options.closeMethod !== false ? options.closeMethod : options.hideMethod;
                    var duration = override && options.closeDuration !== false ?
                        options.closeDuration : options.hideDuration;
                    var easing = override && options.closeEasing !== false ? options.closeEasing : options.hideEasing;
                    if ($(':focus', $toastElement).length && !override) {
                        return;
                    }
                    clearTimeout(progressBar.intervalId);
                    return $toastElement[method]({
                        duration: duration,
                        easing: easing,
                        complete: function () {
                            removeToast($toastElement);
                            clearTimeout(intervalId);
                            if (options.onHidden && response.state !== 'hidden') {
                                options.onHidden();
                            }
                            response.state = 'hidden';
                            response.endTime = new Date();
                            publish(response);
                        }
                    });
                }

                function delayedHideToast() {
                    if (options.timeOut > 0 || options.extendedTimeOut > 0) {
                        intervalId = setTimeout(hideToast, options.extendedTimeOut);
                        progressBar.maxHideTime = parseFloat(options.extendedTimeOut);
                        progressBar.hideEta = new Date().getTime() + progressBar.maxHideTime;
                    }
                }

                function stickAround() {
                    clearTimeout(intervalId);
                    progressBar.hideEta = 0;
                    $toastElement.stop(true, true)[options.showMethod](
                        {duration: options.showDuration, easing: options.showEasing}
                    );
                }

                function updateProgress() {
                    var percentage = ((progressBar.hideEta - (new Date().getTime())) / progressBar.maxHideTime) * 100;
                    $progressElement.width(percentage + '%');
                }
            }

            function getOptions() {
                return $.extend({}, getDefaults(), toastr.options);
            }

            function removeToast($toastElement) {
                if (!$container) { $container = getContainer(); }
                if ($toastElement.is(':visible')) {
                    return;
                }
                $toastElement.remove();
                $toastElement = null;
                if ($container.children().length === 0) {
                    $container.remove();
                    previousToast = undefined;
                }
            }

        })();
    });
}(typeof define === 'function' && define.amd ? define : function (deps, factory) {
    if (typeof module !== 'undefined' && module.exports) { //Node
        module.exports = factory(require('jquery'));
    } else {
        window.toastr = factory(window.jQuery);
    }
}));
