import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

def test_add_multiple_choices():
    question = Question(title='q1')
    choice_1 = question.add_choice('Choice 1', False)
    choice_2 = question.add_choice('Choice 2', True)
    
    assert len(question.choices) == 2
    assert question.choices[0].text == 'Choice 1'
    assert question.choices[1].text == 'Choice 2'
    assert not question.choices[0].is_correct
    assert question.choices[1].is_correct

def test_set_correct_choices_with_invalid_choice_id():
    question = Question(title='q1')
    choice_1 = question.add_choice('Choice 1', False)
    choice_2 = question.add_choice('Choice 2', False)
    
    with pytest.raises(Exception):
        question.set_correct_choices([choice_1.id, 'invalid_id'])

def test_remove_choice():
    question = Question(title='q1')
    choice = question.add_choice('Choice 1', True)
    choice_id = choice.id
    
    question.remove_choice_by_id(choice_id)
    
    assert len(question.choices) == 0

def test_remove_all_choices():
    question = Question(title='q1')
    question.add_choice('Choice 1', True)
    question.add_choice('Choice 2', False)
    
    question.remove_all_choices()
    
    assert len(question.choices) == 0

def test_select_valid_choice():
    question = Question(title='q1')
    choice_1 = question.add_choice('Choice 1', True)
    selected = question.select_choices([choice_1.id])
    
    assert selected == [choice_1.id]

def test_select_invalid_choice():
    question = Question(title='q1')
    choice_1 = question.add_choice('Choice 1', True)
    
    with pytest.raises(Exception):
        question.select_choices([choice_1.id, "invalid_id"])

def test_select_more_than_max_selections():
    question = Question(title='q1', max_selections=1)
    choice_1 = question.add_choice('Choice 1', True)
    choice_2 = question.add_choice('Choice 2', False)
    
    with pytest.raises(Exception):
        question.select_choices([choice_1.id, choice_2.id])

def test_set_correct_choices():
    question = Question(title='q1')
    choice_1 = question.add_choice('Choice 1', False)
    choice_2 = question.add_choice('Choice 2', False)
    
    question.set_correct_choices([choice_1.id])
    
    assert choice_1.is_correct
    assert not choice_2.is_correct

def test_add_choice_with_invalid_text():
    question = Question(title='q1')
    
    with pytest.raises(Exception):
        question.add_choice('', False)
    
    with pytest.raises(Exception):
        question.add_choice('a' * 101, False)

def test_unique_question_ids():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    
    assert question1.id != question2.id