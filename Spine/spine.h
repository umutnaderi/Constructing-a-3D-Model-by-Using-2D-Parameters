#ifndef SPINE_H
#define SPINE_H

#pragma once
#include "vertebra.h"
#include <iostream>

using namespace std;

class Spine{
public:
    vector <Vertebrae> Vector_Vertebrae;
    Spine(){
        Vertebrae v1, v2, v3, v4, v5;
        Vector_Vertebrae.push_back(v1);
        Vector_Vertebrae.push_back(v2);
        Vector_Vertebrae.push_back(v3);
        Vector_Vertebrae.push_back(v4);
        Vector_Vertebrae.push_back(v5);
    }
    ~Spine(){
    }
private:

};


#endif // SPINE_H
