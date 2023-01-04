import openai
import streamlit as st


def get_answer(raw_text, metodo):
    prompt = metodo.pre_prompt + raw_text + metodo.post_prompt
    openai.organization= st.secrets.openai.org
    openai.api_key = st.secrets.openai.key
    response = openai.Completion.create(
        model = metodo.model,
        prompt = prompt,
        temperature = metodo.temperatura,
        max_tokens = metodo.max_tokens,
        top_p = metodo.top_p,
        frequency_penalty = metodo.frequency_penalty,
        presence_penalty = metodo.presence_penalty,
        stop = metodo.stop

        
    )
    return response.choices[0].text

# crear una clase llamada metodo que tenga los atributos pre_prompt, post_prompt y los 
# parametros del modelo de lenguaje
class Metodo:
  def __init__(self, pre_prompt, post_prompt, model, temperatura, max_tokens, top_p, frequency_penalty, presence_penalty):
    self.pre_prompt = pre_prompt
    self.post_prompt = post_prompt
    self.model = model
    self.temperatura = temperatura
    self.max_tokens = max_tokens
    self.top_p = top_p
    self.frequency_penalty = frequency_penalty
    self.presence_penalty = presence_penalty
    self.stop = ']'

# crear una lista de objetos de la clase metodo
extraccion_relaciones = Metodo(
        pre_prompt = 'A list of pairs (a, b), where every pair is a relation between \
            concepts present in the following text:\n\n"',
        post_prompt = 'relation_list= [',
        model = "text-davinci-003",
        temperatura = 0,
        max_tokens = 300,
        top_p = 1.0,
        frequency_penalty = 0.0,
        presence_penalty = 0.0
    )
resumen = Metodo(
        pre_prompt = 'A summary of the following text:\n\n"',
        post_prompt = 'summary= "',
        model = "text-davinci-003",
        temperatura = 0,
        max_tokens = 200,
        top_p = 1.0,
        frequency_penalty = 0.0,
        presence_penalty = 0.0
    )
extraccion_entidades = Metodo(
        pre_prompt = 'A list of entities present in the following text:\n\n"',
        post_prompt = 'entity_list= [',
        model = "text-davinci-003",
        temperatura = 0,
        max_tokens = 300,
        top_p = 1.0,
        frequency_penalty = 0.0,
        presence_penalty = 0.0
    )
extraccion_sentimientos = Metodo(
        pre_prompt = 'A list of sentiments present in the following text:\n\n"',
        post_prompt = 'sentiment_list= [',
        model = "text-davinci-003",
        temperatura = 0,
        max_tokens = 300,
        top_p = 1.0,
        frequency_penalty = 0.0,
        presence_penalty = 0.0
    )
extraccion_conceptos = Metodo(
        pre_prompt = 'A list of concepts present in the following text:\n\n"',
        post_prompt = 'concept_list= [',
        model = "text-davinci-003",
        temperatura = 0,
        max_tokens = 300,
        top_p = 1.0,
        frequency_penalty = 0.0,
        presence_penalty = 0.0
    )
extraccion_preguntas = Metodo(
        pre_prompt = 'A list of questions that can be answered by the following text:\n\n"',
        post_prompt = 'question_list= [',
        model = "text-davinci-003",
        temperatura = 0,
        max_tokens = 300,
        top_p = 1.0,
        frequency_penalty = 0.0,
        presence_penalty = 0.0
    )
extraccion_respuestas = Metodo(
        pre_prompt = 'A list of answers to the following questions:\n\n"',
        post_prompt = 'answer_list= [',
        model = "text-davinci-003",
        temperatura = 0,
        max_tokens = 300,
        top_p = 1.0,
        frequency_penalty = 0.0,
        presence_penalty = 0.0
    )



