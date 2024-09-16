document.addEventListener('DOMContentLoaded', function() {
    const display = document.getElementById('display');
    const buttons = document.querySelectorAll('button');
    let expression = ''; 
    buttons.forEach(button => {
        button.addEventListener('click', function() {
            const value = button.textContent;

            if (value === 'C') {
                clear();
            } else if (value === '=') {
                calculate();
            } else if (value === 'Del') {
                deleteLast();
            } else if (value === '+/-') {
                toggleSign();
            } else {
                if (value === '+' || value === '-' || value === '*' || value === '/') {
                  
                    expression += ' ' + value + ' ';
                } else {
                    
                    expression += value;
                }
    
                display.value = expression;
            }
        });
    });

    function clear() {
        expression = '';
        display.value = '';
    }

    function calculate() {
        
        const tokens = expression.split(/\s+/);
        let result = parseFloat(tokens[0]);
        for (let i = 1; i < tokens.length; i += 2) {
            const operator = tokens[i];
            const nextValue = parseFloat(tokens[i + 1]);
            switch (operator) {
                case '+':
                    result += nextValue;
                    break;
                case '-':
                    result -= nextValue;
                    break;
                case '*':
                    result *= nextValue;
                    break;
                case '/':
                    if (nextValue !== 0) {
                        result /= nextValue;
                    } else {
                        display.value = 'Error: Division by zero';
                        return;
                    }
                    break;
                default:
                    break;
            }
        }
        display.value = result;
        expression = '';
    }

    function deleteLast() {
        if (expression !== '') {
            expression = expression.replace(/(?:\d*\.?\d+|\+|-|\*|\/|\+\/-)$/, '');
            display.value = expression;
        }
    }

});
