def postprocess_output(model_output):
    """
    Process the output from the voice detection model.

    Args:
        model_output (dict): The raw output from the model, containing predictions and other relevant data.

    Returns:
        dict: A processed output containing only the relevant information.
    """
    processed_output = {}

    # Extract relevant information from the model output
    if 'predictions' in model_output:
        processed_output['predictions'] = model_output['predictions']
    
    if 'confidence' in model_output:
        processed_output['confidence'] = model_output['confidence']
    
    # Additional processing can be added here as needed

    return processed_output


def summarize_results(processed_output):
    """
    Summarize the processed output for easier interpretation.

    Args:
        processed_output (dict): The processed output from the model.

    Returns:
        str: A summary string of the results.
    """
    summary = "Voice Detection Results:\n"
    
    if 'predictions' in processed_output:
        summary += f"Predictions: {processed_output['predictions']}\n"
    
    if 'confidence' in processed_output:
        summary += f"Confidence: {processed_output['confidence']:.2f}\n"
    
    return summary