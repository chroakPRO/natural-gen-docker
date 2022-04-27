CREATE TABLE public.results (
    id SERIAL,
    original INT,
    factors VARCHAR(1000)
);

INSERT INTO public.results 
    (original, factors)
VALUES
    (2, '2'),
    (3, '3'),
    (4, '2*2'),
    (5, '5'),
    (6, '2*3'),
    (7, '7'),
    (8, '2*2*2'),
    (9, '3*3');
