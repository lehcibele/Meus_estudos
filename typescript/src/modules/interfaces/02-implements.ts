export const bootstrap = (): void => {
    interface Resume {
        fullName: string;
        email: string;
        skills: Skill[];
        addSkill: (skill: Skill) => boolean // O ? indica que é opcional
    }

    interface Skill {
        name: string;
        level: 'beginner' | 'intermediate' | 'advanced'
    }

    //classe MyResume que tem a estrutura definida pela interface Resume
    class MyResume implements Resume {
        constructor(
            public fullName: string,
            public email: string,
            public skills: Skill[],
        ){}

        addSkill(skill: Skill): boolean {
            const initialLength = this.skills.length
            this.skills.push(skill)
            return this.skills.length > initialLength
        }
    }

    const myResume = new MyResume(
        'Leticia', 
        'leticia@gmail.com',
        [],
    );

    myResume.addSkill( {name: 'javascript', level: 'advanced'} );
    myResume.addSkill({name: 'TypeScript', level: 'beginner'} );
    console.log(myResume);

    // classe MyResume que tem a estrutura definida na interface Resume
    // const MyResume: Resume = {
    //     fullName: 'Leticia',
    //     email: 'leticia@gmail.com',
    //     skills: [
    //         {name: 'javascript', level: 'advanced'},
    //         {name: 'TypeScript', level: 'beginner'},
    //     ]
    // }

    // console.log(MyResume);

};