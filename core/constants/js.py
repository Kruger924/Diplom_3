DRAG_AND_DROP: str = (
    """
    const dataTransfer = new DataTransfer();

    ['dragstart', 'dragenter', 'dragover', 'drop', 'dragend'].forEach(eventType => {
        const e = new DragEvent(eventType, { bubbles: true, cancelable: true, dataTransfer });
        (eventType === 'dragstart' || eventType === 'dragend' ? arguments[0] : arguments[1]).dispatchEvent(e);
    });
    """
)